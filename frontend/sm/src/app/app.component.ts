import { Component } from '@angular/core';
import { MatDialog } from '@angular/material/dialog';
import { AddStudentDialogComponent } from './add-student-dialog/add-student-dialog.component';
import { UpdateStudentComponent } from './update-student/update-student.component';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'sm';
  
  constructor(private dialog: MatDialog) {}

  openAddStudentDialog(): void {
    const dialogRef = this.dialog.open(AddStudentDialogComponent, {
      width: '400px' // Adjust the width as needed
    });

    // Optionally handle the dialog close event if needed
    dialogRef.afterClosed().subscribe(result => {
      if (result) {
        console.log('Dialog was closed with result:', result);
      }
    });
  }

  openUpdateOptionsDialog(): void {
    const dialogRef = this.dialog.open(UpdateStudentComponent, {
      width: '400px' // Adjust the width as needed
    });

    // Optionally handle the dialog close event if needed
    dialogRef.afterClosed().subscribe(result => {
      if (result) {
        console.log('Dialog was closed with result:', result);
      }
    });
  }

}


