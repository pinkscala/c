pragma solidity ^0.8;

import "hardhat/console.sol";

contract school {
    struct Student{
        int roll;
        string fname;
    }

    int public student_count = 0;
    Student[] students;

    function add_student(int roll, string memory fname) public {
        Student memory stud = Student(roll, fname);
        students.push(stud);
        student_count++;
    }

    fallback() external {
        console.log("fallback called!!");
    }

    function view_student(int roll) public view returns (Student memory stud){
        Student memory studd = Student(roll,"Not Available");
        for (uint256 i = 0; i < students.length; i++) {
            if(students[i].roll == roll){
                return students[i];
            }
        }
        return studd;
    }
    
    
}