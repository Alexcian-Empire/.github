import requests, time; 


def fetch_t(version: str, headers: str, email_r: str = "", pass_r: str = ""): 
    email: str = ""; 
    password: str = ""; 
    if email_r=="": email=str(input("Enter Discord Email: ")); 
    if pass_r=="": password=str(input("Enter Password: ")); 
    login_data = { 
            "login": email, 
            "password": password, 
            "captcha_key": None 
    }; 
    def inner(): 
        return requests.post( 
            f"https://discord.com/api/{version}/auth/login", 
            json=login_data, 
            headers=headers 
            ); 
    i: int=0; 
    while i<15: 
        resp = inner(); 
        if resp.status_code == 200: 
            tkn = resp.json()["token"]; 
            print("Received Token: ", tkn); 
            return tkn; 
        print("Failed: ", resp.text); 
        i+=1; 
        time.sleep(10); 
    print("Exiting "); return -1; 


headers = { 
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)", 
        "Content-Type": "application/json" 
} 

if __name__=="__main__": 
    vers: str = "v9"; ## API Version 
    fetch_t(vers, headers); 
    