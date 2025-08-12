import csv
from vehicle_management import Sedan, Truck, SUV, Minivan, OptionalFeature

class VehicleRepository:
    def __init__(self, filename):
        self.filename = filename

    def get_inventory(self):
        return self.load_vehicles_from_csv()

    def save_vehicles_to_csv(self, vehicles):
        with open(self.filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Type', 'Model', 'Base Price', 'Color', 'Model Year', 'Additional Attribute', 'Optional Features'])
            for vehicle in vehicles:
                writer.writerow(vehicle.to_csv_row())

    def load_vehicles_from_csv(self):
        vehicles = []
        try:
            with open(self.filename, mode='r', newline='') as file:
                reader = csv.reader(file)
                next(reader)  
                for row in reader:
                    if len(row) < 6:  
                        print(f"Error processing row: {row}. Row doesn't have enough columns.")
                        continue
                    vehicle_type = row[0]
                    if vehicle_type == 'Sedan':
                        vehicle = Sedan.from_csv_row(row)
                    elif vehicle_type == 'Truck':
                        vehicle = Truck.from_csv_row(row)
                    elif vehicle_type == 'SUV':
                        vehicle = SUV.from_csv_row(row)
                    elif vehicle_type == 'Minivan':
                        vehicle = Minivan.from_csv_row(row)
                    else:
                        continue  # Skip rows with unknown vehicle types
                    vehicles.append(vehicle)
        except FileNotFoundError:
            print(f"File {self.filename} not found.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        return vehicles

    def add_vehicle(self, vehicle):
        vehicles = self.load_vehicles_from_csv()
        vehicles.append(vehicle)
        self.save_vehicles_to_csv(vehicles)

    def remove_vehicle(self, vehicle_type, model):
        vehicles = self.load_vehicles_from_csv()
        removed = False
        new_vehicles = []

        for vehicle in vehicles:
            if vehicle.model == model and type(vehicle).__name__ == vehicle_type:
                removed = True
            else:
                new_vehicles.append(vehicle)

        if removed:
            self.save_vehicles_to_csv(new_vehicles)

        return removed
    
    def sort_by_price(self, vehicle):
        return vehicle.calculate_final_price()
    
    def search_vehicles(self, criteria, value):
        matching_vehicles = []
        vehicles = self.load_vehicles_from_csv()

        if criteria.lower() == "most expensive":
            if not vehicles:
                print("No vehicles available.")
                return None

            max_price = None
            most_expensive_vehicle = None
            for vehicle in vehicles:
                price = vehicle.calculate_final_price()
                if max_price is None or price > max_price:
                    max_price = price
                    most_expensive_vehicle = vehicle
            if most_expensive_vehicle:
                return [most_expensive_vehicle]
            else:
                print("No matching vehicles found.")
                return None

        elif criteria.lower() == "least expensive":
            if not vehicles:
                print("No vehicles available.")
                return None

            min_price = None
            least_expensive_vehicle = None
            for vehicle in vehicles:
                price = vehicle.calculate_final_price()
                if min_price is None or price < min_price:
                    min_price = price
                    least_expensive_vehicle = vehicle
            if least_expensive_vehicle:
                return [least_expensive_vehicle]
            else:
                print("No matching vehicles found.")
                return None

        for vehicle in vehicles:
            if vehicle is not None:  # Check if vehicle data is valid
                if criteria.lower() == "model":
                    if value.lower() in vehicle.model.lower():
                        matching_vehicles.append(vehicle)
                elif criteria.lower() == "color":
                    if value.lower() in vehicle.color.lower():
                        matching_vehicles.append(vehicle)
                elif criteria.lower() == "model year":
                    if str(vehicle.model_year) == value:
                        matching_vehicles.append(vehicle)
            else:
                print("Error: Invalid vehicle data")

        if matching_vehicles:
            print("Matching vehicles found:")
        else:
            print("No matching vehicles found.")
            if not vehicles:
                print("No vehicles available.")

        return matching_vehicles

class OrderRepository:
    def __init__(self, filename):
        self.__filename = filename

    def save_orders_to_csv(self, orders):
        with open(self.__filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Vehicle Model', 'Vehicle Color', 'Vehicle Model Year', 'Optional Features', 'Total Price'])
            for order in orders:
                writer.writerow(order.to_csv_row())

    def get_orders(self):
        orders = []
        try:
            with open(self.__filename, mode='r', newline='') as file:
                reader = csv.reader(file)
                next(reader)  # Skip the header if there is one
                for row in reader:
                    if not row:  # Skip empty rows
                        continue
                    try:
                        order = Order.from_csv_row(row)
                        orders.append(order)
                    except IndexError as e:
                        print(f"Error processing row: {row} - {e}")
            return orders
        except FileNotFoundError:
            print(f"File {self.__filename} not found.")
            return []
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return []

class Order:
    def __init__(self, vehicle_model, vehicle_color, vehicle_model_year, optional_features, total_price):
        self.__vehicle_model = vehicle_model
        self.__vehicle_color = vehicle_color
        self.__vehicle_model_year = vehicle_model_year
        self.__optional_features = optional_features
        self.__total_price = total_price

    def to_csv_row(self):
        return [self.__vehicle_model, self.__vehicle_color, self.__vehicle_model_year, ','.join([feature.name for feature in self.__optional_features]), self.__total_price]

    @classmethod
    def from_csv_row(cls, row):
        vehicle_model = row[0]
        vehicle_color = row[1]
        vehicle_model_year = int(row[2])
        optional_features = [OptionalFeature[feature.strip()] for feature in row[3].split(',')]
        total_price = float(row[4])  
        return cls(vehicle_model, vehicle_color, vehicle_model_year, optional_features, total_price)


class VehicleCustomization:
    @staticmethod
    def customize_vehicle(vehicle):
        print("Customizing vehicle...")
        print("Available optional features:")
        for i, feature in enumerate(OptionalFeature, start=1):
            print(f"{i}. {feature.name} - ${feature.value}")

        while True:
            choice = input("Enter the number of the feature to add: ").strip()
            if choice.isdigit():
                choice = int(choice)
                if 1 <= choice <= len(OptionalFeature):
                    selected_feature = list(OptionalFeature)[choice - 1]
                    vehicle.add_optional_feature(selected_feature)  # Add selected feature
                    print(f"{selected_feature.name} added to the vehicle.")
                    break
                else:
                    print("Invalid choice. Please enter a number within the range.")
            else:
                print("Invalid input. Please enter a number.")

        # Calculate and print total price
        total_price = vehicle.calculate_final_price()
        print(f"Total price after customization: ${total_price}")


class VehicleManagementSystem:
    def __init__(self, vehicle_repository, order_repository):
        self.__vehicle_repository = vehicle_repository
        self.__order_repository = order_repository

    def remove_vehicle(self, vehicle_type, model):
        print("Enter details of the vehicle to remove:")
        vehicle_type = input("Enter vehicle type (Sedan, Truck, SUV, Minivan): ")
        model = input("Enter model: ")

        success = self.__vehicle_repository.remove_vehicle(vehicle_type, model)
        if success:
            print("Vehicle removed successfully.")
        else:
            print("Vehicle not found.")

    def search_vehicles(self, criteria):
        matching_vehicles = []
        all_vehicles = self.__vehicle_repository.load_vehicles_from_csv()

        for vehicle in all_vehicles:
            if criteria.lower() in vehicle.model().lower():
                matching_vehicles.append(vehicle)

        if matching_vehicles:
            print("Matching vehicles found:")
            for idx, vehicle in enumerate(matching_vehicles, 1):
                print(f"{idx}. {vehicle}")
        else:
            print("No matching vehicles found.")

    def create_order(self, vehicle, optional_features):
        order = Order(vehicle, optional_features)
        self.__order_repository.save_orders([order])
        return order

    def display_available_vehicles(self):
        available_vehicles = self.__vehicle_repository.load_vehicles_from_csv()

        if available_vehicles:
            print("Available vehicles:")
            for idx, vehicle in enumerate(available_vehicles, 1):
                print(f"{idx}. {vehicle}")
        else:
            print("No vehicles available.")

    def add_vehicle(self, vehicle):
        self.__vehicle_repository.add_vehicle(vehicle)

