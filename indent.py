ussd = input('the USSD CODE')
if ussd == '*312#':
    print("""
     1. Buy Data Plan
     2. Betting Agent Plan
     3. Gift Data Plan
     4. Share Data Plan
     5. Check Data Balance
     6. Manage Data Plan
     0. Exit
          """)
    user = input ('select your option')
    if user == '1':
        print("""
          Buy Data Plans
          1. Proceed (Auto-Renew)
          2. Proceed (One-off)
          99. Back
          0. Exit
        """)
    
    value = input ('select option')
    if value == '1':
        print("""
              1. Mini Plans
              2. Monthly Plans
              3. Mega Plans
              4. Super Mega Plans
              5. Special Data Offer
              6. Social Bundles
              7. Night and weekend Plans
              99. Back
              0. Exit
              """)
else:
    print("""
          Sorry, Dear customer Our code as Change to
          1. *310# - To check balance
          2. *312# - To buy data balance
          """)
    code = input ('Seclect option')
    if code == '1':
        print("""
                Your credit balance is 1000.19 NGN valid until 13-03-2024.
                special data plans!
                N300=1GB, 1DAY. dial *301# to subcribe.
              """)
    else:
        print('Incorrect code pls try again later, Thank You!')
    value = input ('Select Option')
    if value == '2':
        print("""
             1. Buy Data Plan
            2. Betting Agent Plan
            3. Gift Data Plan
            4. Share Data Plan
            5. Check Data Balance
            6. Manage Data Plan
            0. Exit
        """)
    else:
        print('Incorrect code pls try again later, Thank You!')
        

