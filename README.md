# udemy
Python script for extracting video times of subsections for courses in Udemy. To use the script copy/paste the text in "Course Content" page into a string variable and run from command line.
  

### Tested for
- Cisco CCNA 200-125 – The Complete Guide to Getting Certified
- AWS Certified Developer - Associate 2018 acloudguru

### TO DO
 - merge tables[] and print_sec_times()
 - regex for validating times
 - clean up code
 

### Notes
- Might not need to explicitly exclude attachments (pdf,zip,docx, etc) since a video time vaildation check also occurs. i.e. final output to table[] might still be correct.
- edge case for "Lab excercise" for CCNA course
