import { ChangeEvent, useState } from "react";

export interface InputFieldProps{
    name:string,
    initialValue:string,
    onChanged:(value:string) => void
};

export default function InputTextField({name, initialValue, onChanged}:InputFieldProps){

    const [value, setValue] = useState(initialValue);
    
    function onValueChanged(event:ChangeEvent<HTMLInputElement>){
        setValue(event.target.value);
        onChanged(event.target.value);
    }

    return <>
        <div>
            <label htmlFor="">{name}</label>
            <input type="text" value={value} onChange={onValueChanged}></input>
        </div>
    </>
}