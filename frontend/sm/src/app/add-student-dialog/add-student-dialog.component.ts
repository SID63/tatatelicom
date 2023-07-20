import { Component } from '@angular/core';
import { MatDialogRef } from '@angular/material/dialog';

@Component({
  selector: 'app-add-student-dialog',
  templateUrl: './add-student-dialog.component.html',
  styleUrls: ['./add-student-dialog.component.css']
})
export class AddStudentDialogComponent {
  // Define form controls for input fields
  name: string = '';
  rollNumber: string = '';
  selectedClass: string = '';
  selectedSection: string = '';
  classTeacher: string = '';
  gpa: number = 0;
  feeStatus: boolean = false;

  // Define arrays for dropdown options
  classes: string[] = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'];
  sections: string[] = ['A', 'B', 'C', 'D'];

  // Inject MatDialogRef to close the dialog
  constructor(public dialogRef: MatDialogRef<AddStudentDialogComponent>) {}

  // Function to save the new student data and close the dialog
  saveStudent(): void {
    // Here, you can save the student data to your backend using HTTP requests.
    // Replace this with your actual data saving logic to the backend.
    console.log('Saving student data:', {
      name: this.name,
      rollNumber: this.rollNumber,
      selectedClass: this.selectedClass,
      selectedSection: this.selectedSection,
      classTeacher: this.classTeacher,
      gpa: this.gpa,
      feeStatus: this.feeStatus
    });

    // Close the dialog after saving the data
    this.dialogRef.close();
  }
  formatLabel(value: number): string {
    if (value >= 10) {
      return Math.round(value / 10) + 'k';
    }

    return `${value}`;
  }
}
