import customtkinter#
import sys
from model.model import Model
import sys
from PIL import Image
import matplotlib.pyplot as plt

from rules_makers.rule_maker2 import RulesMaker2

class GUI:
    def __init__(self, root):
        
        self.root = root
        self.root.geometry("750x650")
        self.root.title("Houses Cost Anti Scammer")
        self.model = Model(RulesMaker2(),1e4)


        self.value = customtkinter.CTkFont(family="Cairo", size=25)
        self.font_title = customtkinter.CTkFont(family="Cairo", size=20)
        self.font_header = customtkinter.CTkFont(family="Cairo", size=18)
        self.font = customtkinter.CTkFont(family="Cairo", size=16)
        self.var_font = customtkinter.CTkFont(family="Cairo", size=18)


        _, ax = plt.subplots()
        x = self.model.price_var.universe 
        for term in self.model.price_var.terms:
            ax.plot(x, self.model.price_var[term].mf, label=term)
        ax.set_title('Price Membership Functions')
        plt.savefig('fuzzy_membership.png')
        self.load_icon = customtkinter.CTkImage(Image.open("fuzzy_membership.png"), size=(350, 250))
        self.image_label = customtkinter.CTkLabel(master=self.root, image=self.load_icon, text="")
        self.image_label.place(relx=0.95, rely=0.25, anchor=customtkinter.E)


        self.create_label("0$", self.value, 0, 0, relx=0.48, rely=0.59)
        self.create_label("sqft_living: 0", self.font, 0, 0, relx=0.48, rely=0.7)
        self.create_label("sqft_lot: 0", self.font, 1, 0, relx=0.48, rely=0.75)
        self.create_label("bathrooms: 0", self.font, 2, 0, relx=0.48, rely=0.8)
        self.create_label("condition: 0", self.font, 3, 0, relx=0.48, rely=0.85)
        self.create_label("bedrooms: 0", self.font, 4, 0, relx=0.48, rely=0.9)
        self.create_label("floors: 0", self.font, 5, 0, relx=0.68, rely=0.7)
        self.create_label("view: 0", self.font, 6, 0, relx=0.68, rely=0.75)
        self.create_label("lat: 0", self.font, 7, 0, relx=0.68, rely=0.8)
        self.create_label("long: 0", self.font, 8, 0, relx=0.68, rely=0.85)
        self.create_label("location_rating: 0", self.font, 9, 0, relx=0.68, rely=0.9)

       
        self.create_label("Please enter the fields:", self.font_header, 1, 0, 2)


        self.create_label("Living:", self.var_font, 2, 0)
        self.icon_button_living = customtkinter.CTkButton(master=root, text="i", width=20, height=20, command=self.membership_living)
        self.icon_button_living.grid(row=2, column=1, sticky='e')

        self.create_label("sqft_living:", self.font, 3, 0)
        self.sqft_living = self.create_entry("sqft_living", 3, 1)

        self.create_label("sqft_lot:", self.font, 4, 0)
        self.sqft_lot = self.create_entry("sqft_lot", 4, 1)

        self.create_label("Amenities:", self.var_font, 5, 0)
        self.icon_button_amenities = customtkinter.CTkButton(master=root, text="i", width=20, height=20, command=self.membership_amenities)
        self.icon_button_amenities.grid(row=5, column=1, sticky='e')

        self.create_label("bathrooms:", self.font, 6, 0)
        self.bathrooms = self.create_entry("bathrooms", 6, 1)

        self.create_label("condition:", self.font, 7, 0)
        self.condition = self.create_entry("condition", 7, 1)

        self.create_label("bedrooms:", self.font, 8, 0)
        self.bedrooms = self.create_entry("bedrooms", 8, 1)

        self.create_label("floors:", self.font, 9, 0)
        self.floors = self.create_entry("floors", 9, 1)

        self.create_label("view:", self.font, 10, 0)
        self.view = self.create_entry("view", 10, 1)

        self.create_label("distance:", self.var_font, 11, 0)
        self.icon_button_distance = customtkinter.CTkButton(master=root, text="i", width=20, height=20, command=self.membership_distance)
        self.icon_button_distance.grid(row=11, column=1, sticky='e')

        self.create_label("lat:", self.font, 12, 0)
        self.lat = self.create_entry("lat", 12, 1)

        self.create_label("long:", self.font, 13, 0)
        self.long = self.create_entry("long", 13, 1)

        self.create_label("location_rating:", self.font, 14, 0)
        self.location_rating = self.create_entry("location_rating", 14, 1)

        self.create_label("The predicted price:", self.font_title, 10, 2, relx=0.48, rely=0.5)

        self.submit_button = customtkinter.CTkButton(master=root, width=270, text="Submit", command=self.get_value)
        self.submit_button.grid(row=15, column=0, columnspan=2,  padx = (25, 10),pady=20)

        

    def create_label(self, text, font, row, column, columnspan=1, relx=None, rely=None):
        if column == 0:  
            padx = (25, 10)
        else:
            padx = (10, 10)
        label = customtkinter.CTkLabel(master=self.root, text=text, font=font)
        if relx is not None and rely is not None:
            label.place(relx=relx, rely=rely)
        else:
            label.grid(row=row, column=column, columnspan=columnspan, sticky='w', pady=5, padx=padx)

    def create_entry(self, placeholder_text, row, column):
        entry = customtkinter.CTkEntry(master=self.root, placeholder_text=placeholder_text)
        entry.grid(row=row, column=column, pady=5, sticky='w')
        return entry

    def get_value(self):
        input_data = {
            'sqft_living': float(self.sqft_living.get()),
            'sqft_lot': float(self.sqft_lot.get()),
            'bathrooms': float(self.bathrooms.get()),
            'condition': float(self.condition.get()),
            'bedrooms': float(self.bedrooms.get()),
            'floors': float(self.floors.get()),
            'view': float(self.view.get()),
            'lat': float(self.lat.get()),
            'long': float(self.long.get()),
            'location_rating': float(self.location_rating.get())
        }

        result = self.model.predict(input_data)
        self.model.price_var.view(sim=self.model.fuzzy_system)
        plt.savefig('fuzzy_price_membership.png')
        plt.close()

        self.load_icon = customtkinter.CTkImage(Image.open("fuzzy_price_membership.png"), size=(350, 250))
        self.image_label = customtkinter.CTkLabel(master=self.root, image=self.load_icon, text="")
        self.image_label.place(relx=0.95, rely=0.25, anchor=customtkinter.E)
        self.update_labels(result, input_data)

    def update_labels(self, result, input_data):
        self.create_label(f"{result}$", self.value, 0, 0, relx=0.48, rely=0.59)
        self.create_label(f"sqft_living: {input_data['sqft_living']}", self.font, 0, 0, relx=0.48, rely=0.7)
        self.create_label(f"sqft_lot: {input_data['sqft_lot']}", self.font, 1, 0, relx=0.48, rely=0.75)
        self.create_label(f"bathrooms: {input_data['bathrooms']}", self.font, 2, 0, relx=0.48, rely=0.8)
        self.create_label(f"condition: {input_data['condition']}", self.font, 3, 0, relx=0.48, rely=0.85)
        self.create_label(f"bedrooms: {input_data['bedrooms']}", self.font, 4, 0, relx=0.48, rely=0.9)
        self.create_label(f"floors: {input_data['floors']}", self.font, 5, 0, relx=0.68, rely=0.7)
        self.create_label(f"view: {input_data['view']}", self.font, 6, 0, relx=0.68, rely=0.75)
        self.create_label(f"lat: {input_data['lat']}", self.font, 7, 0, relx=0.68, rely=0.8)
        self.create_label(f"long: {input_data['long']}", self.font, 8, 0, relx=0.68, rely=0.85)
        self.create_label(f"location_rating: {input_data['location_rating']}", self.font, 9, 0, relx=0.68, rely=0.9)

    def membership_living(self):
        self.model.input_vars['size'].view(sim=self.model.fuzzy_system)


    def membership_amenities(self):
        self.model.input_vars['amenities'].view(sim=self.model.fuzzy_system)


    def membership_distance(self):
        self.model.input_vars['location'].view(sim=self.model.fuzzy_system)



if __name__ == "__main__":
    root = customtkinter.CTk()
    app = GUI(root)
    root.mainloop()
