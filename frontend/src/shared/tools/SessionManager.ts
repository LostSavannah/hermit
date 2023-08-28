import { Token } from "../types/Token";

const tokenKeyName = "Token";

export function GetSessionToken():Token | null{
    let result: Token | null = null;
    let token = sessionStorage.getItem(tokenKeyName);
    if(token){
        result = JSON.parse(token) as Token;
    }
    return result;
}

export function SetSessionToken(token:Token): Token | null{
    sessionStorage.setItem(tokenKeyName, JSON.stringify(token));
    return GetSessionToken();
}

export function RemoveSessionToken(){
    sessionStorage.removeItem(tokenKeyName);
}