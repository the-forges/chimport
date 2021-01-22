# Process to follow

- [x] Get filename from args
- [x] Verify file exists
- [x] Read in data to pandas
- [ ] Normalize data
    - [x] Select necessary columns
    - [ ] Check for valid data
        - [ ] Consider ways to transform invalid emails so that they become valid
        - [ ] filter out blanks in some colums
    - [ ] Store invalid data for manual correction later
        - [x] use pandas to convert DF from csv read to a csv
        - [ ] Move data from importable csv to a new csv
        - [ ] Save new csv for later
- [ ] Import to mail chimp