import { Component } from '@angular/core';
import { MatDialogRef } from '@angular/material/dialog';

@Component({
  selector: 'app-update-student',
  templateUrl: './update-student.component.html',
  styleUrls: ['./update-student.component.css']
})
export class UpdateStudentComponent {
  // Define form controls for input fields
  rollNumberUpdated: string = '';
  updateBy: string = '';
  gpaUpdated: number = 0;
  feeStatusUpdated: boolean = false;

  // Define arrays for dropdown options
  options: string[] = ['GPA','Fee Status'];
  sections: string[] = ['A', 'B', 'C', 'D'];

  // Inject MatDialogRef to close the dialog
  constructor(public dialogRef: MatDialogRef<UpdateStudentComponent>) {}

  // Function to save the new student data and close the dialog
  saveStudent(): void {
    // Here, you can save the student data to your backend using HTTP requests.
    // Replace this with your actual data saving logic to the backend.
    console.log('Saving student data:', {
      rollNumberUpdated: this.rollNumberUpdated,
      updateBy: this.updateBy,
      gpaUpdated: this.gpaUpdated,
      feeStatusUpdated: this.feeStatusUpdated
    });

    // Close the dialog after saving the data
    this.dialogRef.close();
  }

}
