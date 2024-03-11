class NewUser:

    check_list = []
    
    def __init__(self, username):
        self.username = username
    
    # method to dictionary to list to easier use
    def convert_data_to_list(self, data):
        for data in data.values():
            for val in data:
                self.check_list.append(val)
                
        return self.check_list
        
    # method to pick plan 
    def pick_plan(self, new_plan, referral_code):
        if referral_code in self.check_list:
            if new_plan == "Basic Plan":
                total = 120_000 - (120_000 * 0.04)
                return total
            elif new_plan == "Standard Plan":
                total = 160_000 - (160_000 * 0.04)
                return total
            elif new_plan == "Premium Plan":
                total = 200_000 - (200_000 * 0.04)
                return total
            else:
                print("Plan doesn't exist")
        else:
            raise Exception("Referral Code doesn't exist")

faizal = NewUser("faizal_icikiwir")

print(faizal.convert_data_to_list(data))

print(faizal.pick_plan("Basic Plan", "shandy-2134"))