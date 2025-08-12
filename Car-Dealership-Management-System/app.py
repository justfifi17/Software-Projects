from repository import VehicleRepository, VehicleCustomization
from vehicle_management import Sedan, Truck, SUV, Minivan

class CarDealershipApp:
    def __init__(self, vehicle_repository):
        self.__vehicle_repository = vehicle_repository

    def show_program_title(self):
        print("Welcome to XYZ Car Dealership's Vehicle Management System")

    def show_menu(self):
        print("1. Add Vehicle")
        print("2. Remove Vehicle")
        print("3. Search Vehicles")
        print("4. Update Vehicle")
        print("5. View Inventory")
        print("6. Exit")

    def process_command(self, choice):
        if choice == "1":
            self.add_vehicle()
        elif choice == "2":
            self.remove_vehicle()
        elif choice == "3":
            self.search_vehicles()
        elif choice == "4":
            self.update_vehicle()
        elif choice == "5":
            self.view_inventory()
        elif choice == "6":
            print("Thank you for using our service :)")
            exit()
        else:
            print("Invalid choice. Please enter a valid option.")


    def add_vehicle(self):
        while True: 
            print("Enter vehicle type:")
            print("1. Sedan")
            print("2. Truck")
            print("3. SUV")
            print("4. Minivan")
            vehicle_type = input("Enter the number corresponding to the vehicle type: ").strip()

            if vehicle_type not in ["1", "2", "3", "4"]:
                print("Invalid input. Please enter a number corresponding to the vehicle type.")
                continue
            
            model = input("Enter model: ")
            color = input("Enter color: ")
            model_year = input("Enter model year: ")

            try:
                model_year = int(model_year)
            except ValueError:
                print("Invalid input. Model year must be an integer.")
                return

            if vehicle_type == "1":
                vehicle = Sedan(model, color, model_year)
            elif vehicle_type == "2":
                cargo_bed_size = input("Enter cargo bed size: ")
                vehicle = Truck(model, color, model_year, cargo_bed_size)
            elif vehicle_type == "3":
                roof_rack_type = input("Enter roof rack type: ")
                vehicle = SUV(model, color, model_year, roof_rack_type)
            elif vehicle_type == "4":
                has_sliding_door = input("Does the minivan have a sliding door? (yes/no): ").lower() == "yes"
                vehicle = Minivan(model, color, model_year, has_sliding_door)
            else:
                print("Invalid vehicle type.")
                return
            
            while True:
                choice = input("Do you want to customize the vehicle with optional features? (yes/no): ").strip().lower()
                if choice in ["yes", "no"]:
                    break
                else:
                    print("Invalid input. Please enter 'yes' or 'no'.")
            
            if choice == "yes":
                VehicleCustomization.customize_vehicle(vehicle)

            total_price = vehicle.calculate_final_price()
            print(f"Total price of the vehicle: ${total_price}")

            self.__vehicle_repository.add_vehicle(vehicle)
            print("Vehicle added successfully.")

            choice = input("Do you want to add another vehicle? (yes/no): ").strip().lower()
            if choice != "yes":
                break

    def remove_vehicle(self):
        print("Enter details of the vehicle to remove:")
        vehicle_type = input("Enter vehicle type (Sedan, Truck, SUV, Minivan): ")
        model = input("Enter model: ")

        if vehicle_type.lower() == "sedan":
            success = self.__vehicle_repository.remove_vehicle("Sedan", model)
        elif vehicle_type.lower() == "truck":
            success = self.__vehicle_repository.remove_vehicle("Truck", model)
        elif vehicle_type.lower() == "suv":
            success = self.__vehicle_repository.remove_vehicle("SUV", model)
        elif vehicle_type.lower() == "minivan":
            success = self.__vehicle_repository.remove_vehicle("Minivan", model)
        else:
            print("Invalid vehicle type.")
            return

        if success:
            print("Vehicle removed successfully.")
        else:
            print("Vehicle not found.")

    def search_vehicles(self):
        print("Search for vehicles:")
        print("1. Search by model")
        print("2. Search by color")
        print("3. Search by model year")
        print("4. Search for most expensive vehicle")
        print("5. Search for least expensive vehicle")
        choice = input("Enter your choice: ").strip()

        if choice in ["1", "2", "3"]:
            criteria = ["model", "color", "model year"][int(choice) - 1]
            value = input(f"Enter the {criteria}: ")
        elif choice == "4":
            criteria = "most expensive"
            value = None
        elif choice == "5":
            criteria = "least expensive"
            value = None
        else:
            print("Invalid choice.")
            return

        found_vehicles = self.__vehicle_repository.search_vehicles(criteria, value)
        if found_vehicles:
            for vehicle in found_vehicles:
                print(f" {vehicle}")
        else:
            print("No vehicles found matching the criteria.")


    def update_vehicle(self):
        print("Enter details of the vehicle to update")
        vehicle_type = input("Enter vehicle type (Sedan, Truck, SUV, Minivan) ")
        model = input("Enter model: ")
        color = input("Enter color: ")
        model_year = input("Enter model year: ")

        # Find the vehicle in the inventory based on the provided details
        matching_vehicles = self.__vehicle_repository.search_vehicles("model", model)
        matching_vehicles = [v for v in matching_vehicles if v.color == color and v.model_year == int(model_year)]


        if matching_vehicles:
            print("Matching vehicles found")
            for idx, vehicle in enumerate(matching_vehicles, 1):
                print(f"{idx}. {vehicle}")

            choice = input("Enter the number of the vehicle to update: ")
            try:
                choice = int(choice)
                if 1 <= choice <= len(matching_vehicles):
                    
                    selected_vehicle = matching_vehicles[choice - 1]
                    print(f"You have selected {selected_vehicle} for updating.")

                    # Prompt the user for new details
                    new_model = input("Enter new model (press Enter to keep current): ")
                    new_color = input("Enter new color (press Enter to keep current): ")
                    new_model_year = input("Enter new model year (press Enter to keep current): ")

                    # Update the vehicle with the new details
                    if new_model:
                        selected_vehicle.model = new_model
                    if new_color:
                        selected_vehicle.color = new_color
                    if new_model_year:
                        selected_vehicle.model_year = int(new_model_year)

                    # Save the changes to the CSV file
                    self.__vehicle_repository.save_vehicles_to_csv([selected_vehicle])

                    print("Vehicle updated successfully.")
                else:
                    print("Invalid choice. Please enter a number within the range.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        else:
            print("No vehicles found matching the provided details.")


    def view_inventory(self):
        inventory = self.__vehicle_repository.get_inventory()
        if inventory:
            print("Current Inventory:")
            for vehicle in inventory:
                print(f" {vehicle}")
        else:
            print("No vehicles in inventory.")

    def save_inventory_to_csv(self):
        self.__vehicle_repository.save_vehicles_to_csv()
        print("Inventory saved to CSV successfully.")

    def load_inventory_from_csv(self):
        self.__vehicle_repository.load_vehicles_from_csv()
        print("Inventory loaded from CSV successfully.")

def main():
    vehicle_repository = VehicleRepository("vehicle_data.csv")
    app = CarDealershipApp(vehicle_repository)
    app.show_program_title()

    while True:
        app.show_menu()
        choice = input("Enter your choice: ")
        app.process_command(choice)


if __name__ == "__main__":
    main()
