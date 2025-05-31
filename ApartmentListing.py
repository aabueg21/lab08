from Apartment import Apartment
from ApartmentListingNode import ApartmentListingNode

class ApartmentListing:
    def __init__(self):
        self.root = None

    def add_apartment(self, apartment):
        if self.root == None:
            self.root = ApartmentListingNode(apartment)
            return
        
        current = self.root
        apt_location = apartment.location.upper()
        apt_size = apartment.size

        while True:
            node_location = current.location
            node_size = current.size

            if apt_location == node_location and apt_size == node_size:
                current.apartments.append(apartment)
                return
            
            elif apt_location < node_location or (apt_location == node_location and apt_size < node_size):
                if current.left == None:
                    current.left = ApartmentListingNode(apartment)
                    current.left.parent = current
                    return
                else:
                    current = current.left
                
            elif apt_location > node_location or (apt_location == node_location and apt_size > node_size):
                if current.right == None:
                    current.right = ApartmentListingNode(apartment)
                    current.right.parent = current
                    return
                else:
                    current = current.right

            else:
                return

        
    def does_apartment_exist(self, apartment):
        current = self.root
        apt_location = apartment.location.upper()
        apt_size = apartment.size

        while current != None:
            node_location = current.location
            node_size = current.size

            if apt_location == node_location and apt_size == node_size:
                for apt in current.apartments:
                    if apt == apartment:
                        return True
            
            elif apt_location < node_location or (apt_location == node_location and apt_size < node_size):
                current = current.left

            else:
                current = current.right
        return False
    
    def inorder(self):
        def inorder_helper(node):
            if node is None:
                return ""
            return inorder_helper(node.left) + str(node) + inorder_helper(node.right)
    
        return inorder_helper(self.root)
    
    def preorder(self):
        def preorder_helper(node):
            if node is None:
                return ""
            return str(node) + preorder_helper(node.left) + preorder_helper(node.right)
    
        return preorder_helper(self.root)
    
    def postorder(self):
        def postorder_helper(node):
            if node is None:
                return ""
            return postorder_helper(node.left) + postorder_helper(node.right) + str(node)
    
        return postorder_helper(self.root)
    
    def get_best_apartment(self, location, size):
        loc = location.upper()
        current = self.root

        while current != None:
            if loc == current.location and size == current.size:
                if not current.apartments:
                    return None
                best = current.apartments[0]
                for apt in current.apartments[1:]:
                    if apt.bedrooms > best.bedrooms:
                        best = apt
                    elif apt.bedrooms == best.bedrooms and apt.rent > best.rent:
                        best = apt
                return best
        
            elif loc < current.location or (loc == current.location and size < current.size):
                current = current.left
            
            else: 
                current = current.right
        
        return None

    def get_worst_apartment(self, location, size):
        loc = location.upper()
        current = self.root

        while current != None:
            if loc == current.location and size == current.size:
                if not current.apartments:
                    return None
                worst = current.apartments[0]
                for apt in current.apartments[1:]:
                    if apt.bedrooms < worst.bedrooms:
                        worst = apt
                    elif apt.bedrooms == worst.bedrooms and apt.rent < worst.rent:
                        worst = apt
                return worst
        
            elif loc < current.location or (loc == current.location and size < current.size):
                current = current.left
            
            else: 
                current = current.right
        
        return None
    
    def get_total_listing_price(self):
        def inorder_helper(node):
            if node is None:
                return 0
            node_total = sum(apt.rent for apt in node.apartments)
            return inorder_helper(node.left) + node_total + inorder_helper(node.right)
    
        return inorder_helper(self.root)
    










