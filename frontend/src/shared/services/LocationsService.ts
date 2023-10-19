import { Location } from "../types/Location";
import { Result } from "../types";
import { Record } from "../types";
import BaseAPIService from "./BaseAPIService";

export default class LocationsService extends BaseAPIService{
    async getMyLocations(){
        let a:Result<number>
        return await this.get<Result<Record<Location>[]>()
    }
}