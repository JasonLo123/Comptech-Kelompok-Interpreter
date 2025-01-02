PROGRAM BIGNUMBER;
    VAR num1,num2,bignum: integer;
BEGIN
    num1:=10;
    num2:=20;
    IF (num1>num2) THEN
        BEGIN
            bignum := num1;
            WRITELN('Big Number is ',bignum);
        END
    ELSE
        BEGIN
            bignum := num2;
            WRITELN('Big Number is ',bignum);
        END;
END.