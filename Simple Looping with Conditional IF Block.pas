PROGRAM LISTODDNUMBER;
    VAR num,oddnum: integer;
BEGIN
    WRITELN('List of Odd Number 1-100:');
    WRITELN;
    FOR num:=1 TO 100 DO
        BEGIN
            IF (num MOD 2)<>0 THEN
                BEGIN
                    oddnum := num;
                    WRITE(oddnum,' ');
                END;
        END;
END.