import { useEffect, useState } from "react";
import { Location } from "../../../types/Location";


export default function useMyLocationsList(){
    const [locations, setLocations] = useState<Location[]>([]);

    useEffect(() => {
        
    }, []);

    return{
        locations
    }
};