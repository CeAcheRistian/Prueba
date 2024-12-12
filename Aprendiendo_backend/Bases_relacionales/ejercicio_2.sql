CREATE DATABASE HackerRank;

USE HackerRank;

CREATE TABLE DifficultyLevel (
	DifficultyLevelID INT NOT NULL AUTO_INCREMENT, 
	Name VARCHAR(20) NOT NULL, 
	IsActive TINYINT DEFAULT 1,
	PRIMARY KEY (DifficultyLevelID)
);

CREATE TABLE Category (
	CategoryID INT NOT NULL AUTO_INCREMENT, 
	Name VARCHAR(20) NOT NULL, 
	IsActive TINYINT DEFAULT 1,
	PRIMARY KEY (CategoryID)
);

CREATE TABLE ProgrammingLanguage (
	ProgrammingLanguageID INT NOT NULL AUTO_INCREMENT, 
	Name VARCHAR(50) NOT NULL, 
	PRIMARY KEY (ProgrammingLanguageID)
);

CREATE TABLE Hacker (
	HackerID VARCHAR(20) NOT NULL, 
	FirstName VARCHAR(50) NOT NULL, 
	LastName VARCHAR(50), 
	Email VARCHAR(100) UNIQUE, 
	PhoneNumber VARCHAR(20),
	CountryCode VARCHAR(3),
	IsActive TINYINT DEFAULT 1,
	PRIMARY KEY (HackerID)
);

CREATE TABLE MenuType (
	MenuTypeID INT NOT NULL AUTO_INCREMENT, 
	Name VARCHAR(20) NOT NULL, 
	IsActive TINYINT DEFAULT 1,
	PRIMARY KEY (MenuTypeID)
);

CREATE TABLE Menu (
	MenuID INT NOT NULL AUTO_INCREMENT, 
	Name VARCHAR(20) NOT NULL, 
	URLSuffix VARCHAR(100), 
	MenuTypeID INT NOT NULL,
	IsActive TINYINT DEFAULT 1,
	PRIMARY KEY (MenuID),
	FOREIGN KEY (MenuTypeID) REFERENCES MenuType(MenuTypeID)
);

CREATE TABLE Challenge (
	ChallengeID INT NOT NULL AUTO_INCREMENT, 
	ChallengeName VARCHAR(50) NOT NULL, 
	Description VARCHAR(50), 
	DifficultyLevelID INT NOT NULL,
	IsActive TINYINT DEFAULT 1,
	PRIMARY KEY (ChallengeID),
	FOREIGN KEY (DifficultyLevelID) REFERENCES DifficultyLevel(DifficultyLevelID)
);

CREATE TABLE ChallengeCategory (
	ChallengeID INT NOT NULL, 
	CategoryID INT NOT NULL, 
	PRIMARY KEY (ChallengeID, CategoryID),
	FOREIGN KEY (ChallengeID) REFERENCES Challenge(ChallengeID),
	FOREIGN KEY (CategoryID) REFERENCES Category(CategoryID)
);

CREATE TABLE HackerChallenge (
	HackerID VARCHAR(20) NOT NULL, 
	ChallengeID INT NOT NULL,
	StartDate DATETIME,
	EnDate DATETIME,
	Score INT,
	ProgrammingLanguageID INT NOT NULL,
	PRIMARY KEY (HackerID, ChallengeID),
	FOREIGN KEY (HackerID) REFERENCES Hacker(HackerID),
	FOREIGN KEY (ChallengeID) REFERENCES Challenge(ChallengeID),
	FOREIGN KEY (ProgrammingLanguageID) REFERENCES ProgrammingLanguage(ProgrammingLanguageID)
);

CREATE TABLE ChallengeMenu (
	ChallengeID INT NOT NULL, 
	MenuID INT NOT NULL,
	PRIMARY KEY (ChallengeID, MenuID),
	FOREIGN KEY (ChallengeID) REFERENCES Challenge(ChallengeID),
	FOREIGN KEY (MenuID) REFERENCES Menu(MenuID)
);

# ---------------------------------------------------
# Tabla intermediaria entre los retos y las clases.
CREATE TABLE ChallengeResource (
	ChallengeID INT NOT NULL, 
	ResourceID INT NOT NULL,
	PRIMARY KEY (ChallengeID, ResourceID),
	FOREIGN KEY (ChallengeID) REFERENCES Challenge(ChallengeID),
	FOREIGN KEY (ResourceID) REFERENCES Resource(ResourceID)
);

# Tabla para la introduccion a los cursos
CREATE TABLE Resource (
    ResourceID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	Name VARCHAR(100) NOT NULL,
    ResourceTypeID TINYINT NOT NULL,
    LanguageID SMALLINT NOT NULL,
    URL VARCHAR(100),

    FOREIGN KEY (ResourceTypeID) REFERENCES ResourceType(ResourceTypeID)
    FOREIGN KEY (LanguageID) REFERENCES Language(LanguageID)
)

# Tabla para el tipo de curso
CREATE TABLE ResourceType (
    ResourceTypeID TINYINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(50) NOT NULL,
	IsActive TINYINT DEFAULT 1
)

# Tabla para el idioma de los cursos
CREATE TABLE Language (
    LanguageID SMALLINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(50) NOT NULL
)


# ---------------------------------------------------
# Tabla para los cursos con toda su información
CREATE TABLE Course (
    CourseID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	Name VARCHAR(100),
    TeacherID INT NOT NULL,
    Description VARCHAR(300) NOT NULL,
    Duration DECIMAL NOT NULL,
	CourseURL VARCHAR(100),
	VideoURL VARCHAR(100),

	FOREIGN KEY (TeacherID) REFERENCES Teacher(TeacherID)
)

CREATE TABLE Teacher (
	TeacherID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	Name VARCHAR(100) NOT NULL,
	IsActive TINYINT DEFAULT 1
)

CREATE TABLE CourseContent (
	ContentID BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	Name VARCHAR(100) NOT NULL,
	Secuence SMALLINT NOT NULL, 
	IsActive TINYINT DEFAULT 1,
	CourseID INT NOT NULL,

	FOREIGN KEY (CourseID) REFERENCES Course(CourseID)
)

# ---------------------------------------------------

CREATE TABLE Bootcamp (
	BootcampID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	Name VARCHAR(100) NOT NULL,
	Description VARCHAR(300) NOT NULL,
	StartDate DATE,
	Duration TINYINT NOT NULL,
	Schedule VARCHAR(100),
	BootcampURL VARCHAR(100),
	VideoURL VARCHAR(100),
	BootcampTeacherID INT NOT NULL,
	BootcampDifficultyID INT NOT NULL,

	FOREIGN KEY (BootcampTeacherID) REFERENCES BootcampTeachers(BootcampTeacherID)
	FOREIGN KEY (BootcampDifficultyID) REFERENCES BootcampDifficulty(DificultyID)
)

CREATE TABLE BootcampContent (
	ContentID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	Name VARCHAR(100) NOT NULL,
	IsActive TINYINT DEFAULT 1,
	BootcampID INT NOT NULL,

	FOREIGN KEY (BootcampID) REFERENCES Bootcamp(BootcampID)
)

CREATE TABLE BootcampDifficulty (
	DificultyID TINYINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	Description VARCHAR(300) NOT NULL
)

CREATE TABLE BootcampTeachers (
	TeacherID INT NOT NULL AUTO_INCREMENT,
	BootcampID INT NOT NULL AUTO_INCREMENT,
	PRIMARY KEY (TeacherID, BootcampID),
	TeacherStatusID TINYINT NOT NULL,

	FOREIGN KEY (TeacherID) REFERENCES Teacher(TeacherID),
	FOREIGN KEY (BootcampID) REFERENCES Bootcamp(BootcampID)
)

CREATE TABLE TeacherStatusID (
	StatusID TINYINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	Descripcion VARCHAR(100),
)

/* 
	Dos ejemplos para seleccionar datos usando JOIN:
	Select * FROM Bootcamp B INNER JOIN BootcampTeachers BT ON B.BootcampID = BT.BootcampID INNER JOIN Teacher T ON T.TeacherID = BT.TeacherID;
	Unimos las tablas Bootcamp, BootcampTeachers y Teacher para obtener los datos de los profesores que imparten los bootcamps asignandole un alias a cada tabla.

	SELECT * FROM Bootcamp B, BootcampTeachers BT, Teacher T WHERE B.BootcampID = BT.BootcampID AND T.TeacherID = BT.TeacherID;
	Lo mismo que el ejemplo anterior pero sin usar INNER JOIN, se hace la unión de las tablas con una coma y se especifica la condición en el WHERE.
*/		