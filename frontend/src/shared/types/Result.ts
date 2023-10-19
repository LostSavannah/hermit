export interface Result<T>{
    value:T|null;
    statusCode:number,
    success:boolean
};