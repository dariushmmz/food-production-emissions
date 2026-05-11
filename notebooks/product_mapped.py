product_mapping = {
    # Grains & Cereals
    'Wheat & Rye (Bread)': ['Wheat', 'Rye', 'Triticale', 'Cereals, primary', 'Mixed grain'],
    'Maize (Meal)': ['Maize (corn)', 'Green corn (maize)', 'Cereals, primary', 'Oil of maize'],
    'Barley (Beer)': ['Barley', 'Beer of barley, malted', 'Cereals, primary'],
    'Oatmeal': ['Oats', 'Cereals, primary'],
    'Rice': ['Rice', 'Cereals, primary'],

    # Root Vegetables & Tubers
    'Potatoes': ['Potatoes', 'Roots and Tubers, Total'],
    'Cassava': ['Cassava, fresh', 'Cassava leaves', 'Roots and Tubers, Total'],
    'Root Vegetables': ['Carrots and turnips', 'Roots and Tubers, Total', 'Edible roots and tubers with high starch or inulin content, n.e.c., fresh'],

    # Sugars
    'Cane Sugar': ['Sugar cane', 'Raw cane or beet sugar (centrifugal only)', 'Sugar Crops Primary'],
    'Beet Sugar': ['Sugar beet', 'Raw cane or beet sugar (centrifugal only)', 'Sugar Crops Primary'],

    # Pulses & Legumes
    'Other Pulses': ['Other pulses n.e.c.', 'Pulses, Total', 'Cow peas, dry', 'Pigeon peas, dry', 'Bambara beans, dry', 'Lupins', 'Vetches'],
    'Peas': ['Peas, dry', 'Peas, green', 'Pulses, Total'],

    # Nuts & Seeds
    'Nuts': ['Treenuts, Total', 'Other nuts (excluding wild edible nuts and groundnuts), in shell, n.e.c.',
             'Walnuts, in shell', 'Pistachios, in shell', 'Cashew nuts, in shell', 'Chestnuts, in shell',
             'Hazelnuts, in shell', 'Brazil nuts, in shell', 'Almonds, in shell', 'Areca nuts'],
    'Groundnuts': ['Groundnuts, excluding shelled', 'Peanut oil', 'Oilcrops, Oil Equivalent'],

    # Soy Products
    'Soymilk': ['Soya beans', 'Skim milk of cows', 'Whole milk powder'],  # Soymilk from soybeans
    'Tofu': ['Soya beans', 'Soya bean oil'],

    # Oils
    'Soybean Oil': ['Soya bean oil', 'Oilcrops, Oil Equivalent'],
    'Palm Oil': ['Palm oil', 'Oil palm fruit', 'Oil of palm kernel', 'Palm kernels', 'Oilcrops, Oil Equivalent'],
    'Sunflower Oil': ['Sunflower-seed oil, crude', 'Sunflower seed', 'Oilcrops, Oil Equivalent'],
    'Rapeseed Oil': ['Rapeseed or canola oil, crude', 'Rape or colza seed', 'Oilcrops, Oil Equivalent'],
    'Olive Oil': ['Olive oil', 'Olives', 'Oilcrops, Oil Equivalent'],

    # Vegetables
    'Tomatoes': ['Tomatoes', 'Vegetables Primary'],
    'Onions & Leeks': ['Onions and shallots, dry (excluding dehydrated)', 'Onions and shallots, green', 'Leeks and other alliaceous vegetables', 'Vegetables Primary'],
    'Brassicas': ['Cabbages', 'Cauliflowers and broccoli', 'Brussels sprouts', 'Vegetables Primary'],
    'Other Vegetables': ['Other vegetables, fresh n.e.c.', 'Vegetables Primary', 'Artichokes', 'Asparagus', 'Okra',
                        'Spinach', 'Lettuce and chicory', 'Pumpkins, squash and gourds', 'Cucumbers and gherkins',
                        'Eggplants (aubergines)', 'Chillies and peppers, green', 'Mushrooms and truffles', 'Green garlic',
                        'String beans', 'Other beans, green', 'Broad beans and horse beans, green'],

    # Fruits
    'Citrus Fruit': ['Citrus Fruit, Total', 'Oranges', 'Tangerines, mandarins, clementines', 'Lemons and limes',
                    'Pomelos and grapefruits', 'Other citrus fruit, n.e.c.'],
    'Bananas': ['Bananas', 'Plantains and cooking bananas', 'Fruit Primary'],
    'Apples': ['Apples', 'Fruit Primary'],
    'Berries & Grapes': ['Grapes', 'Strawberries', 'Raspberries', 'Blueberries', 'Cranberries', 'Currants',
                        'Gooseberries', 'Other berries and fruits of the genus vaccinium n.e.c.', 'Fruit Primary'],
    'Wine': ['Wine', 'Grapes'],
    'Other Fruit': ['Other fruits, n.e.c.', 'Fruit Primary', 'Avocados', 'Pineapples', 'Papayas', 'Mangoes, guavas and mangosteens',
                   'Dates', 'Figs', 'Kiwi fruit', 'Persimmons', 'Pears', 'Quinces', 'Apricots', 'Peaches and nectarines',
                   'Plums and sloes', 'Cherries', 'Sour cherries', 'Other stone fruits', 'Other pome fruits',
                   'Other tropical fruits, n.e.c.', 'Cantaloupes and other melons', 'Watermelons'],

    # Stimulants & Sweets
    'Coffee': ['Coffee, green', 'Other stimulant, spice and aromatic crops, n.e.c.'],
    'Dark Chocolate': ['Cocoa beans', 'Sugar Crops Primary'],  # Cocoa + sugar

    # Meat - Beef
    'Beef (beef herd)': ['Meat of cattle with the bone, fresh or chilled', 'Beef and Buffalo Meat, primary',
                        'Cattle', 'Meat, Total', 'Meat of buffalo, fresh or chilled'],  # Added buffalo meat
    'Beef (dairy herd)': ['Meat of cattle with the bone, fresh or chilled', 'Beef and Buffalo Meat, primary',
                         'Cattle', 'Raw milk of cattle', 'Meat, Total', 'Meat of buffalo, fresh or chilled'],  # Added buffalo meat

    # Meat - Lamb & Pork & Poultry
    'Lamb & Mutton': ['Meat of sheep, fresh or chilled', 'Sheep and Goat Meat', 'Sheep', 'Meat, Total'],
    'Pig Meat': ['Meat of pig with the bone, fresh or chilled', 'Meat, Total', 'Swine / pigs'],
    'Poultry Meat': ['Meat of chickens, fresh or chilled', 'Meat of turkeys, fresh or chilled', 'Meat, Poultry',
                    'Meat of ducks, fresh or chilled', 'Meat of geese, fresh or chilled', 'Chickens', 'Turkeys',
                    'Ducks', 'Geese', 'Other birds', 'Meat of pigeons and other birds n.e.c.', 'Meat, Total'],

    # Dairy
    'Milk': ['Raw milk of cattle', 'Raw milk of goats', 'Raw milk of sheep', 'Raw milk of buffalo',
            'Raw milk of camel', 'Milk, Total'],
    'Cheese': ['Cheese (All Kinds)', 'Cheese from whole cow milk', 'Cheese from skimmed cow milk',
              'Cheese from milk of goats, fresh or processed', 'Cheese from milk of sheep, fresh or processed',
              'Cheese from milk of buffalo, fresh or processed'],
    'Eggs': ['Hen eggs in shell, fresh', 'Eggs Primary', 'Eggs from other birds in shell, fresh, n.e.c.'],

    # Seafood
    'Fish (farmed)': ['Fish, farmed'],  # Note: FAO may have specific fish items
    'Shrimps (farmed)': ['Shrimps, farmed'],  # Note: FAO may have specific crustacean items
}
