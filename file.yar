rule xls_48661
{
    strings:
        
        $magic =  {D0 CF 11}
    condition:
        ($magic at 0) 
}        