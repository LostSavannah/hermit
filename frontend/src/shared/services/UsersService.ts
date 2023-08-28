import Result from "../types/Result";
import { Token } from "../types/Token";
import BaseAPIService from "./BaseAPIService"

export interface LoginParams{
    name:string,
    password:string
};

export default class UsersService extends BaseAPIService{
    async login({name, password}:LoginParams){
        return await this.post<LoginParams, Token>("users/login", {name, password});
    }
}