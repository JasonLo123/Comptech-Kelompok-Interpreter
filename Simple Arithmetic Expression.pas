PROGRAM SUMANDAVERAGE;
VAR num1,num2,num3: integer;
    sum:integer;
    avg:real;
BEGIN
    num1:=10;
    num2:=20;
    num3:=30;
    sum:=num1+num2+num3;
    avg:=sum/3;
    WRITELN('Num1 is ',num1);
    WRITELN('Num2 is ',num2);
    WRITELN('Num3 is ',num3);
    WRITELN('Sum 3 numbers is ',sum);
    WRITELN('Average is ',avg);
END.