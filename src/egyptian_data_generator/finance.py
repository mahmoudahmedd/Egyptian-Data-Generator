from egyptian_data_generator.helpers import Helpers


class Finance:
    def americanexpressCreditCardNumber(self): 
        return self.generateCreditCardNumber("americanexpress")
    
    def discoverCreditCardNumber(self): 
        return self.generate("discover")
    
    def mastercardCreditCardNumber(self): 
        return self.generateCreditCardNumber("mastercard")
    
    def visa16CreditCardNumber(self): 
        return self.generateCreditCardNumber("visa16")
    
    def visa13CreditCardNumber(self):
        return self.generateCreditCardNumber("visa13")

    def generateCreditCardNumber(self, _type):
        card_types = ["americanexpress", "visa13", "visa16", "mastercard", "discover"]
        
        def prefill(t):
            def_length = 16
            
            if t == card_types[0]:
                return [3, Helpers.intBetween(4,7)], 13
            elif t == card_types[1] or t == card_types[2]:
                if t.endswith("16"):
                    return [4], def_length - 1
                else:
                    return [4], 12
            elif t == card_types[3]:
                return [5, Helpers.intBetween(1,5)], def_length - 2
            elif t == card_types[4]:
                return [6, 0, 1, 1], def_length - 4
            else:
                return [], def_length
        
        def finalize(nums):
            check_sum = 0

            check_offset = (len(nums) + 1) % 2
            
            for i, n in enumerate(nums):
                if (i + check_offset) % 2 == 0:
                    n_ = n*2
                    check_sum += n_ -9 if n_ > 9 else n_
                else:
                    check_sum += n
            return nums + [10 - (check_sum % 10) ]

        initial, rem = prefill(_type.lower())
        so_far = initial + [Helpers.intBetween(1,9) for x in range(rem - 1)]
        return "".join(map(str,finalize(so_far)))


