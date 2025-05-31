from Apartment import Apartment
from ApartmentListingNode import ApartmentListingNode
from ApartmentListing import ApartmentListing

class TestApartment:
    def test_init(self):
        apt = Apartment("Mountains", 0, 0, 0)
        assert apt.location == "MOUNTAINS"
        assert apt.size == 0
        assert apt.bedrooms == 0
        assert apt.rent == 0

    def test_gt(self):
        apt1 = Apartment("Downtown", 900, 2, 1000)
        apt2 = Apartment("Ocean Side", 950, 2, 1100) # Test by location
        assert apt2 > apt1

        apt1 = Apartment("Downtown", 900, 2, 1000)
        apt2 = Apartment("Downtown", 950, 2, 1100) # Test by size
        assert apt2 > apt1

        apt1 = Apartment("Downtown", 900, 2, 1000)
        apt2 = Apartment("Downtown", 900, 1, 1100) # Test by bedrooms
        assert apt1 > apt2

        apt1 = Apartment("Downtown", 900, 2, 1000)
        apt2 = Apartment("Downtown", 900, 2, 1100) # Test by rent
        assert apt2 > apt1

        
    def test_lt(self):
        apt1 = Apartment("Downtown", 900, 2, 1000)
        apt2 = Apartment("Ocean Side", 950, 2, 1100) # Test by location
        assert apt1 < apt2

        apt1 = Apartment("Downtown", 900, 2, 1000)
        apt2 = Apartment("Downtown", 950, 2, 1100) # Test by size
        assert apt1 < apt2

        apt1 = Apartment("Downtown", 900, 2, 1000)
        apt2 = Apartment("Downtown", 900, 1, 1100) # Test by bedrooms
        assert apt2 < apt1

        apt1 = Apartment("Downtown", 900, 2, 1000)
        apt2 = Apartment("DOwntown", 900, 2, 1100) # Test by rent
        assert apt1 < apt2
        
    def test_eq(self):
        apt1 = Apartment("Downtown", 900, 2, 1000)
        apt2 = Apartment("Downtown", 900, 2, 1000) # Test by rent
        assert apt1 == apt2
    
    def test_str(self):
        apt1 = Apartment("Downtown", 900, 2, 1000)
        assert apt1.__str__() == "Location: DOWNTOWN, Size: 900 sqft, Bedrooms: 2, Rent: $1000"

class TestApartmentListingNode:
    def test_init(self):
        apt1 = Apartment("Downtown", 900, 2, 1000)
        node = ApartmentListingNode(apt1)

        assert node.location == "DOWNTOWN"
        assert node.size == 900
        assert node.apartments == [apt1]
        assert node.parent == None
        assert node.left == None
        assert node.right == None

    def test_get_location(self):
        apt1 = Apartment("Downtown", 900, 2, 1000)
        node = ApartmentListingNode(apt1)
        assert node.location == "DOWNTOWN"
    
    def test_get_size(self):
        apt1 = Apartment("Downtown", 900, 2, 1000)
        node = ApartmentListingNode(apt1)
        assert node.size == 900
    
    def test_get_parent(self):
        apt1 = Apartment("Downtown", 900, 2, 1000)
        node = ApartmentListingNode(apt1)
        assert node.get_parent() == None
    
    def test_set_parent(self):
        apt1 = Apartment("Downtown", 900, 2, 1000)
        apt2 = Apartment("Ocean Side", 950, 2, 1100)
        node1 = ApartmentListingNode(apt1)
        node2 = ApartmentListingNode(apt2)
        node1.set_parent(node2)
        assert node1.parent == node2
    
    def test_get_left(self):
        apt1 = Apartment("Downtown", 900, 2, 1000)
        node1 = ApartmentListingNode(apt1)
        assert node1.get_left() == None
    
    def test_set_left(self):
        apt1 = Apartment("Downtown", 900, 2, 1000)
        apt2 = Apartment("Beach", 950, 2, 1100)
        node1 = ApartmentListingNode(apt1)
        node2 = ApartmentListingNode(apt2)
        node1.set_left(node2)
        assert node1.left == node2
    
    def test_get_right(self):
        apt1 = Apartment("Downtown", 900, 2, 1000)
        node1 = ApartmentListingNode(apt1)
        assert node1.get_right() == None
    
    def test_set_right(self):
        apt1 = Apartment("Downtown", 900, 2, 1000)
        apt2 = Apartment("Ocean Side", 950, 2, 1100)
        node1 = ApartmentListingNode(apt1)
        node2 = ApartmentListingNode(apt2)
        node1.set_right(node2)
        assert node1.right == node2
    
    def test_str(self):
        apt1 = Apartment("Downtown", 900, 2, 1000)
        apt2 = Apartment("Beach", 950, 2, 1100)
        node = ApartmentListingNode(apt1)
        node.apartments.append(apt2)
        assert node.__str__() == "Location: DOWNTOWN, Size: 900 sqft, Bedrooms: 2, Rent: $1000\n\
Location: BEACH, Size: 950 sqft, Bedrooms: 2, Rent: $1100\n"

class TestApartmentListing:
    def test_init(self):
        listing = ApartmentListing()
        assert listing.root == None

    def test_add_apartment(self):
        bst = ApartmentListing()
        apt1 = Apartment("Mountain View", 900, 1, 2500)
        apt2 = Apartment("Mountain View", 900, 2, 3000)
        apt3 = Apartment("Oakland", 1000, 3, 3500)
        apt4 = Apartment("Napa", 950, 2, 3000)
        
        bst.add_apartment(apt1)
        bst.add_apartment(apt2)
        bst.add_apartment(apt3)
        bst.add_apartment(apt4)

        assert bst.root.apartments == [apt1, apt2]
        assert bst.root.right.apartments == [apt3]
        assert bst.root.right.left.apartments == [apt4]
        assert bst.root.left == None

        
    def test_does_apartment_exist(self):
        bst = ApartmentListing()
        apt1 = Apartment("Mountain View", 900, 1, 2500)
        apt2 = Apartment("Mountain View", 900, 2, 3000)
        apt3 = Apartment("Oakland", 1000, 3, 3500)
        apt4 = Apartment("Napa", 950, 2, 3000)
        
        bst.add_apartment(apt1)
        bst.add_apartment(apt2)
        bst.add_apartment(apt3)

        assert bst.does_apartment_exist(apt4) == False
        assert bst.does_apartment_exist(apt3) == True
    
    def test_inorder(self):
        bst = ApartmentListing()
        apt1 = Apartment("Mountain View", 900, 1, 2500)
        apt2 = Apartment("Mountain View", 900, 2, 3000)
        apt3 = Apartment("Oakland", 1000, 3, 3500)
        apt4 = Apartment("Napa", 950, 2, 3000) # Goes ALL THE WAY right first
        
        bst.add_apartment(apt1)
        bst.add_apartment(apt2)
        bst.add_apartment(apt3)
        bst.add_apartment(apt4)

        assert bst.inorder() == \
"""\
Location: MOUNTAIN VIEW, Size: 900 sqft, Bedrooms: 1, Rent: $2500
Location: MOUNTAIN VIEW, Size: 900 sqft, Bedrooms: 2, Rent: $3000
Location: NAPA, Size: 950 sqft, Bedrooms: 2, Rent: $3000
Location: OAKLAND, Size: 1000 sqft, Bedrooms: 3, Rent: $3500
"""

    def test_preorder(self):
        bst = ApartmentListing()
        apt1 = Apartment("Mountain View", 900, 1, 2500)
        apt2 = Apartment("Mountain View", 900, 2, 3000)
        apt3 = Apartment("Oakland", 1000, 3, 3500)
        apt4 = Apartment("Burbank", 950, 2, 3000) 
        
        bst.add_apartment(apt1)
        bst.add_apartment(apt2)
        bst.add_apartment(apt3)
        bst.add_apartment(apt4)

        assert bst.preorder() == \
"""\
Location: MOUNTAIN VIEW, Size: 900 sqft, Bedrooms: 1, Rent: $2500
Location: MOUNTAIN VIEW, Size: 900 sqft, Bedrooms: 2, Rent: $3000
Location: BURBANK, Size: 950 sqft, Bedrooms: 2, Rent: $3000
Location: OAKLAND, Size: 1000 sqft, Bedrooms: 3, Rent: $3500
"""
    
    def test_postorder(self):
        bst = ApartmentListing()
        apt1 = Apartment("Mountain View", 900, 1, 2500)
        apt2 = Apartment("Mountain View", 900, 2, 3000)
        apt3 = Apartment("Oakland", 1000, 3, 3500)
        apt4 = Apartment("Burbank", 950, 2, 3000) 
        
        bst.add_apartment(apt1)
        bst.add_apartment(apt2)
        bst.add_apartment(apt3)
        bst.add_apartment(apt4)

        assert bst.postorder() == \
"""\
Location: BURBANK, Size: 950 sqft, Bedrooms: 2, Rent: $3000
Location: OAKLAND, Size: 1000 sqft, Bedrooms: 3, Rent: $3500
Location: MOUNTAIN VIEW, Size: 900 sqft, Bedrooms: 1, Rent: $2500
Location: MOUNTAIN VIEW, Size: 900 sqft, Bedrooms: 2, Rent: $3000
"""
    
    def test_get_best_apartment(self):
        bst = ApartmentListing()
        apt1 = Apartment("Mountain View", 900, 1, 2500)
        apt2 = Apartment("Mountain View", 900, 2, 3000)
        apt3 = Apartment("Oakland", 1000, 3, 3500)
        apt4 = Apartment("Burbank", 950, 2, 3000) 
        
        bst.add_apartment(apt1)
        bst.add_apartment(apt2)
        bst.add_apartment(apt3)
        bst.add_apartment(apt4)

        assert bst.get_best_apartment("Mountain View", 900) == apt2

    def test_get_worst_apartment(self):
        bst = ApartmentListing()
        apt1 = Apartment("Mountain View", 900, 1, 2500)
        apt2 = Apartment("Mountain View", 900, 2, 3000)
        apt3 = Apartment("Oakland", 1000, 3, 3500)
        apt4 = Apartment("Burbank", 950, 2, 3000) 
        
        bst.add_apartment(apt1)
        bst.add_apartment(apt2)
        bst.add_apartment(apt3)
        bst.add_apartment(apt4)

        assert bst.get_worst_apartment("Mountain View", 900) == apt1
        
    
    def test_get_total_listing_price(self):
        bst = ApartmentListing()
        apt1 = Apartment("Mountain View", 900, 1, 2500)
        apt2 = Apartment("Mountain View", 900, 2, 3000)
        apt3 = Apartment("Oakland", 1000, 3, 3500)
        apt4 = Apartment("Burbank", 950, 2, 3000) 
        
        bst.add_apartment(apt1)
        bst.add_apartment(apt2)
        bst.add_apartment(apt3)
        bst.add_apartment(apt4)

        assert bst.get_total_listing_price() == 12000
        
        
