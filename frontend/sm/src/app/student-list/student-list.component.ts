import { Component } from '@angular/core';

@Component({
  selector: 'app-student-list',
  templateUrl: './student-list.component.html',
  styleUrls: ['./student-list.component.css']
})
export class StudentListComponent {
  
  showTable: boolean = false;
  searchQuery = '';
  onViewStudentsClick(): void {
    // Here, you can fetch the student data from your backend service using HTTP requests.
    // For demonstration purposes, let's assume we have the data in an array called "students".
    // Replace this with your actual data fetching logic from the backend.
    // For example, this.students = this.backendService.getStudents();
    this.showTable = true;
  }

  // You can also define the "students" array here to hold the student data when fetched from the backend.
  // students: any[] = [];
}
