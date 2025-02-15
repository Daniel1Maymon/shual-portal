# Shual Portal

This project is designed to manage and create businesses for miluimnikim soldiers from the Sayeret Givati. The system allows easy creation, updating, deletion, and retrieval of businesses, while maintaining privacy and organized data management.

## Technologies Used

- **FastAPI** - Fast and simple web framework for building APIs.
- **SQLAlchemy** - ORM (Object-Relational Mapping) for interacting with databases.
- **PostgreSQL** - Relational database for managing business data.
- **Pydantic** - For data validation and schema definition.

## Key Features

- Create a new business
- Update business details
- Search and filter businesses based on various criteria
- Health check endpoint to check server status

## How to Run the Project

1. **Install Dependencies**:
   Use `pip` to install all dependencies listed in `requirements.txt`:
   ```bash
   pip install -r requirements.txt


2. **Run the Server: Start the server using uvicorn:**
    ```
    uvicorn app.main:app --reload
    ```

3. **Access the API: Once the server is running, you can access the API at http://127.0.0.1:8000.**

4. **Interactive API Docs: FastAPI provides interactive documentation. You can access it at http://127.0.0.1:8000/docs.**


## Endpoints

### **POST /business**
- **Description**: Create a new business.
- **Request Body**: 
    ```json
    {
        "business_name": "Fox Coffee",
        "owner_name": "John Doe",
        "email": "john@fox.com",
        "phone_number": "123-456-7890",
        "recruitment_batch": "2020",
        "domain": "Coffee",
        "description": "A cozy café",
        "contact_info": "Downtown Street 12",
        "logo": "https://example.com/logo.png"
    }
    ```

### **GET /business/{id}**
- **Description**: Retrieve business by ID.
- **Request Body**: None.

### **PATCH /business/{id}/contact-info**
- **Description**: Update business contact info.
- **Request Body**: 
    ```json
    {
        "contact_info": "New Address, Tel Aviv"
    }
    ```

### **PUT /business/{id}**
- **Description**: Update full business details.
- **Request Body**: 
    ```json
    {
        "business_name": "Updated Name",
        "owner_name": "New Owner",
        "email": "new_email@example.com",
        "phone_number": "999-999-9999",
        "recruitment_batch": "2021",
        "domain": "Updated Category",
        "description": "Updated business description",
        "contact_info": "Updated address",
        "logo": "https://example.com/new_logo.png"
    }
    ```

### **DELETE /business/{id}**
- **Description**: Delete business by ID.
- **Request Body**: None.

### **GET /search/businesses**
- **Description**: Search businesses by name.
- **Request Body**: None.

### **GET /businesses/filter**
- **Description**: Filter businesses by category, location, or recruitment batch.
- **Request Body**: None.

### **GET /businesses**
- **Description**: Retrieve all businesses.
- **Request Body**: None.

### **GET /healthcheck**
- **Description**: Check server health.
- **Request Body**: None.


