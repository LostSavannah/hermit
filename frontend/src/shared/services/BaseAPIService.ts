import { GetSessionToken } from "../tools/SessionManager";
import { Result } from "../types/Result";

export default class BaseAPIService{
    protected baseUrl: string = "http://localhost:8080";

    async post<T, TResult>(url:string, data:T, isAnonymous:boolean|null = null):Promise<Result<TResult>>{
        return await new Promise<Result<TResult>>((resolve, reject) => {
            fetch(`${this.baseUrl}/${url}`, {
                method: 'POST',
                headers:{
                    "Content-Type": "application/json",
                    ...(isAnonymous? {} : {"Token": GetSessionToken()?.token ?? ""})
                },
                body: JSON.stringify(data)
            })
            .catch(err => {
                resolve({
                    value: null,
                    statusCode: 500,
                    success: false
                })
            })
            .then(response => {
                if(response){
                    if(response.status != 200){
                        resolve({
                            value:null,
                            statusCode: response.status,
                            success: false
                        })
                    }else{
                        response.json().then(json => {
                            resolve({
                                value: json as TResult,
                                statusCode: response.status,
                                success: true
                            })
                        });
                    }
                }
            }); 
        });
    }

    async get<TResult>(url:string): Promise<Result<TResult>>{
        return await new Promise<Result<TResult>>((resolve, reject) => {
            fetch(`${this.baseUrl}/${url}`, {
                method: 'GET',
                headers: {
                    "Content-Type": "application/json",
                    "Token": GetSessionToken()?.token ?? ""
                }
            })
            .catch(err => {
                resolve({
                    value: null,
                    statusCode: 500,
                    success: false
                })
            })
            .then(response => {
                if(response){
                    if(response.status != 200){
                        resolve({
                            value:null,
                            statusCode: response.status,
                            success: false
                        })
                    }else{
                        response.json().then(json => {
                            resolve({
                                value: json as TResult,
                                statusCode: response.status,
                                success: true
                            })
                        });
                    }
                }
            }); 
        });
    }
}