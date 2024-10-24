#include <iostream>  // for input/output
#include <string>    // for using strings
#include <vector>    // for using vectors (STL)
using namespace std;

class Patient {
   public:
    string id;
    string name;
    string age;
    string gender;
    string contacts;
    string diagnosis;
    string physician;
    string department;

    Patient(string id, string name, string age, string gender, string contacts,
            string diagnosis, string physician, string department) {
        this->id = id;
        this->name = name;
        this->age = age;
        this->gender = gender;
        this->contacts = contacts;
        this->diagnosis = diagnosis;
        this->physician = physician;
        this->department = department;
        this->assign_physician();
    }

    string to_string() { return this->age; }

    void assign_physician() {
        if (this->diagnosis == "breast" || this->diagnosis == "lung") {
            this->physician = "Dr. Susan Jones";
            this->department = "J";
        } else {
            this->physician = "Dr. Ben Smith";
            this->department = "S";
        }
    }
};

int main() {
    while (true) {
    }
    return 0;
}