# Python CRUD Application for input score student [Teacher]

A comprehensive Python application for managing [Data Entity] data with Create, Read, Update, and Delete (CRUD) operations.

## Teacher Understanding

This project caters to the [Education/School Domain] Education, specifically addressing the need to manage [Data Entity] data efficiently. [Data Entity] plays a crucial role in [Explain the importance of data entity in Education processes].

    ** Benefits:
    * Better data accuracy and consistency
    * Streamlined data management process
    * Better decision-making through available data
    * Operate efficiently for optimization in the field of education.

    ** Target Users:
    This application is designed for teachers who want to input student grades and in addition there is also about student personal data 
    to facilitate those who are related to students and student guardians.

## Features

* **Create:**
     *  Add data entry of grade 10,11,12 students' grades data with important details especially student grades and student's parent number for other additions such as               student's personal data such as height, weight, skin color, parent's name and residence.
     * Apply validation rules to ensure that the student's parent number is not the same as another student's parent number.
* **Read:**
   * Search and retrieve specific student grade data by applying filters based on the student's parent number.
   * Display comprehensive information for each student in a user-usable format.
* **Update:**
    * Modify existing student grade data to reflect changes in student name, gender, class, subject and grade, as available.
    * Provides clear confirmation or error messages based on the success or failure of the update.
* **Delete:**
   * Enables deletion of unwanted student grade data with appropriate authorization checks.

## Installation

1. **Prerequisites:**
    * Python version (specify the required version)
    * Additional dependencies (list any required packages)

2. **Installation:**
    ```bash
    git clone https://github.com/<your-username>/<your-repo-name>.git
    cd <your-repo-name>
    pip install -r requirements.txt  # If using a requirements.txt file
    ```

3. **Database Setup (if applicable):**
    Follow specific instructions for configuring your database connection, aligning with the business's chosen database management system.

## Usage

1. **Run the application:**
    ```bash
    python main.py
    ```

2. **CRUD Operations:**
    * **Create:** Add a new [Data Entity] record, for example, especially student grades and student's parent number for 
      other additions such as student's personal data such as height, weight, skin color, parent's name and residence.
    * **Read:** Search and retrieve student information by name, NIS, or other relevant criteria.
    * **Update:** Modify Student details, such as updating their address or contact details.
    * **Delete:** Remove a customer record from the system (with appropriate authorization, if applicable).


 **Data Model** 
  This project uses a list of dictionaries to present student grade data. each student's grade record is stored in the 
   system. with the :
  **NIS** = integer type as the primary key.
  **name** = string type "description name student"
  **gender** = string type "description gender student"
  **parent** = string type "description parent student"
   **place** = string type "description place student"
   **weight** = integer type "description weight student"
   **height** = integer type "description height student"
   **class** = integer type "description class student"
   **score** = integer type "description score student"
   **vocational** = string type "description vocational student"
   **subject** = string type "description subject student"

   **Contributing**
   We welcome contributions to this project! Please feel free to open a pull request, sent to miftahfurqaanull@gmail.com or submit an issue if you encounter any problems or     have suggestions for improvements.

