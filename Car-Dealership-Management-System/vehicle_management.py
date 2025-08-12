from enum import Enum
from abc import ABC, abstractmethod

class VehicleType(Enum):
    SEDAN = "SEDAN"
    TRUCK = "TRUCK"
    SUV = "SUV"
    MINIVAN = "MINIVAN"

class OptionalFeature(Enum):
    ENHANCED_SAFETY_FEATURES = 3000
    SECURITY = 1000
    ENTERTAINMENT_SYSTEM = 2000
    SUNROOF = 2500


    @property
    def name(self):
        return self._name_

    @property
    def value(self):
        return self._value_



class Vehicle(ABC):
    def __init__(self, model, base_price, color, model_year):
        self.__model = model
        self.__base_price = base_price
        self.__color = color
        self.__model_year = model_year
        self.__optional_features = []

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        self.__model = model

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        self.__color = color

    @property
    def model_year(self):
        return self.__model_year
    

    @model_year.setter
    def model_year(self, model_year):
        self.__model_year = model_year

    @property
    def base_price(self):
        return self.__base_price

    @abstractmethod
    def calculate_final_price(self):
        pass

    def add_optional_feature(self, feature):
        self.__optional_features.append(feature)

    def remove_optional_feature(self, feature):
        if feature in self.__optional_features:
            self.__optional_features.remove(feature)

    def get_optional_features(self):
        return self.__optional_features

    def calculate_optional_features_cost(self):
        total_cost = 0
        for feature in self.__optional_features:
            total_cost += feature.value
        return total_cost

    def __str__(self):
        optional_features_str = ', '.join(feature.name for feature in self.__optional_features)
        return f"Vehicle Type: {type(self).__name__}, Model: {self.__model}, Base Price: ${self.__base_price}, Color: {self.__color}, Model Year: {self.__model_year}, Optional Features: {optional_features_str}"


class Sedan(Vehicle):
    def __init__(self, model, color, model_year, optional_feature=None):
        super().__init__(model, 30000, color, model_year)

    def calculate_final_price(self):
        total_price = self.base_price + self.calculate_optional_features_cost()
        
        return total_price
    
    def to_csv_row(self):
        # Check if optional features are present
        optional_features = self.get_optional_features()
        optional_features_str = ''
        if optional_features:
            for feature in optional_features:
                if optional_features_str:
                    optional_features_str += ', '  
                optional_features_str += feature.name
        return ['Sedan', self.model, self.color, self.model_year, 'N/A', optional_features_str, 'N/A']
    
    @classmethod
    def from_csv_row(cls, row):
        try: 
            model = row[1]
            color = row[2]
            model_year = int(row[3])
            if row[4] != 'N/A':  # Check if optional features are provided
                optional_feature = OptionalFeature[row[4]]
            else:
                optional_feature = None
            return cls(model, color, model_year, optional_feature)
        except IndexError:
            print(f"Error processing row: {row}. Row doesn't have enough columns.")
            return None  # Return None to indicate failure
    

class Truck(Vehicle):
    def __init__(self, model, color, model_year, cargo_bed_size, optional_feature=None):
        super().__init__(model, 35000, color, model_year)
        self.__cargo_bed_size = cargo_bed_size

    def get_cargo_bed_size(self):
        return self.__cargo_bed_size

    def calculate_final_price(self):
        total_price = self.base_price + self.calculate_optional_features_cost()
        return total_price
    
    def to_csv_row(self):
        # Check if optional features are present
        optional_features = self.get_optional_features()
        optional_features_str = ''
        if optional_features:
            for feature in optional_features:
                if optional_features_str:
                    optional_features_str += ', '  
                optional_features_str += feature.name
        return ['Truck', self.model, self.color, self.model_year, self.get_cargo_bed_size(), optional_features_str, '']
    
    @classmethod
    def from_csv_row(cls, row):
        try: 
            model = row[1]
            color = row[2]
            model_year = int(row[3])
            cargo_bed_size = row[4]
            return cls(model, color, model_year, cargo_bed_size)
        except IndexError:
            print(f"Error processing row: {row}. Row doesn't have enough columns.")
            return None  # Return None to indicate failure

class SUV(Vehicle):
    def __init__(self, model, color, model_year, roof_rack_type, optional_feature=None):
        super().__init__(model, 40000, color, model_year)
        self.__roof_rack_type = roof_rack_type

    def get_roof_rack_type(self):
        return self.__roof_rack_type

    def calculate_final_price(self):
        total_price = self.base_price + self.calculate_optional_features_cost()
        return total_price
    
    def to_csv_row(self):
        # Check if optional features are present
        optional_features = self.get_optional_features()
        optional_features_str = ''
        if optional_features:
            for feature in optional_features:
                if optional_features_str:
                    optional_features_str += ', '  
                optional_features_str += feature.name
        return ['SUV', self.model, self.color, self.model_year, self.get_roof_rack_type(), optional_features_str, '']
    
    @classmethod
    def from_csv_row(cls, row):
        try: 
            model = row[1]
            color = row[2]
            model_year = int(row[3])
            roof_rack_type = row[4]
            return cls(model, color, model_year, roof_rack_type)
        except IndexError:
            print(f"Error processing row: {row}. Row doesn't have enough columns.")
            return None  # Return None to indicate failure

class Minivan(Vehicle):
    def __init__(self, model, color, model_year, has_sliding_door, optional_feature=None):
        super().__init__(model, 45000, color, model_year)
        self.__has_sliding_door = has_sliding_door

    def calculate_final_price(self):
        total_price = self.base_price + self.calculate_optional_features_cost()
        return total_price
    
    def to_csv_row(self):
        # Check if optional features are present
        optional_features = self.get_optional_features()
        optional_features_str = ''
        if optional_features:
            for feature in optional_features:
                if optional_features_str:
                    optional_features_str += ', '  
                optional_features_str += feature.name
        sliding_door = "Sliding Door" if self.__has_sliding_door else "No sliding door"
        return ['Minivan', self.model, self.color, self.model_year, sliding_door, optional_features_str, '']
    
    @classmethod
    def from_csv_row(cls, row):
        try: 
            model = row[1]
            color = row[2]
            model_year = int(row[3])
            has_sliding_door = row[4].lower() == "yes"  
            return cls(model, color, model_year, has_sliding_door)
        except IndexError:
            print(f"Error processing row: {row}. Row doesn't have enough columns.")
            return None  # Return None to indicate failure