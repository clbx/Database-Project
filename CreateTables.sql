CREATE TABLE `Courses` (
    `ID` int  NOT NULL ,
    `Code` varchar  NOT NULL ,
    `Name` varchar  NOT NULL ,
    `Instructor` int  NOT NULL ,
    `Status` varchar  NOT NULL ,
    `Seats` varchar  NOT NULL ,
    `Time` varchar  NOT NULL ,
    `Credits` int  NOT NULL ,
    PRIMARY KEY (
        `ID`
    )
);

CREATE TABLE `Professors` (
    `ID` int  NOT NULL ,
    `Fname` varchar  NOT NULL ,
    `Lname` varchar  NOT NULL ,
    `DeptID` int  NOT NULL ,
    `Level` varchar  NOT NULL ,
    `Years` int  NOT NULL ,
    PRIMARY KEY (
        `ID`
    )
);

CREATE TABLE `Students` (
    `ID` int  NOT NULL ,
    `Fname` varchar  NOT NULL ,
    `Lname` varchar  NOT NULL ,
    `DeptID` int  NOT NULL ,
    `Major` varchar  NOT NULL ,
    `Minor` varchar  NOT NULL ,
    `AdvisorID` int  NOT NULL ,
    PRIMARY KEY (
        `ID`
    )
);

CREATE TABLE `Dept` (
    `ID` int  NOT NULL ,
    `Name` varchar  NOT NULL ,
    `Chair` int  NOT NULL ,
    PRIMARY KEY (
        `ID`
    )
);

CREATE TABLE `CourseRecords` (
    `StudentID` int  NOT NULL ,
    `CourseCode` int  NOT NULL ,
    `Grade` int  NOT NULL ,
    PRIMARY KEY (
        `StudentID`
    )
);

ALTER TABLE `Courses` ADD CONSTRAINT `fk_Courses_Instructor` FOREIGN KEY(`Instructor`)
REFERENCES `Professors` (`ID`);

ALTER TABLE `Professors` ADD CONSTRAINT `fk_Professors_DeptID` FOREIGN KEY(`DeptID`)
REFERENCES `Dept` (`ID`);

ALTER TABLE `Students` ADD CONSTRAINT `fk_Students_AdvisorID` FOREIGN KEY(`AdvisorID`)
REFERENCES `Professors` (`ID`);

ALTER TABLE `Dept` ADD CONSTRAINT `fk_Dept_Chair` FOREIGN KEY(`Chair`)
REFERENCES `Professors` (`ID`);

ALTER TABLE `CourseRecords` ADD CONSTRAINT `fk_CourseRecords_StudentID` FOREIGN KEY(`StudentID`)
REFERENCES `Students` (`ID`);

ALTER TABLE `CourseRecords` ADD CONSTRAINT `fk_CourseRecords_CourseCode` FOREIGN KEY(`CourseCode`)
REFERENCES `Courses` (`ID`);
