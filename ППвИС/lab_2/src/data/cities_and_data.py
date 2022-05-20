import random

class New_Yourk_cities:
    def __init__(self):
        self.cities_names = 'Albany Amsterdam Auburn Babylon Batavia Beacon Bedford Binghamton Bronx Brooklyn Buffalo Chautauqua Cheektowaga Clinton Cohoes Coney Island Cooperstown Corning Cortland Crown Point Dunkirk East Aurora East Hampton Eastchester Elmira Flushing Forest Hills Fredonia Garden City Geneva Glens Falls Gloversville Great Neck Hammondsport Harlem Hempstead Herkimer Hudson Huntington Hyde Park Ilion Ithaca Jamestown Johnstown Kingston Lackawanna Lake Placid Levittown Lockport Mamaroneck Manhattan Massena Middletown Mineola Mount Vernon New Paltz New Rochelle New Windsor New York City Newburgh Niagara Falls North Hempstead Nyack Ogdensburg Olean Oneida Oneonta Ossining Oswego Oyster Bay Palmyra Peekskill Plattsburgh Port Washington Potsdam Poughkeepsie Queens Rensselaer Rochester Rome Rotterdam Rye Sag Harbor Saranac Lake Saratoga Springs Scarsdale Schenectady Seneca Falls Southampton Staten Island Stony Brook Stony Point Syracuse Tarrytown Ticonderoga Tonawanda Troy Utica Watertown Watervliet Watkins Glen West Seneca White Plains Woodstock Yonkers'.split(' ')

    def get_city(self):
        return self.cities_names[random.randint(0,len(self.cities_names)-1)]

class Data_of_travel:
    def __init__(self):
        self.day = None	
        self.month = None
        self.year = None

        self.hour = None
        self.min = None
        self.sec = None
    
    def get_dep_data(self):
        self.day = random.randint(1, 31)
        self.month = random.randint(1, 12)
        self.year = random.randint(2000, 2005)

        self.hour = random.randint(1, 24)
        self.min = random.randint(1, 60)
        self.sec = random.randint(1, 60)

        return str(str(random.randint(1, 31))+'/'
        +str(random.randint(1, 12))+'/'
        +str(random.randint(2000, 2005))+' '
        +str(random.randint(1, 24))+':'
        +str(random.randint(1, 60))+':'
        +str(random.randint(1, 60)))

    def get_arr_data(self):
        self.day = random.randint(1, 31)
        self.month = random.randint(1, 12)
        self.year = random.randint(2005, 2010)

        self.hour = random.randint(1, 24)
        self.min = random.randint(1, 60)
        self.sec = random.randint(1, 60)

        return str(str(random.randint(1, 31))+'/'
        +str(random.randint(1, 12))+'/'
        +str(random.randint(2005, 2010))+' '
        +str(random.randint(1, 24))+':'
        +str(random.randint(1, 60))+':'
        +str(random.randint(1, 60)))
