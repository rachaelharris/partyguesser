# partyguesser
This program is based upon a survey released by the [New York Times](https://www.nytimes.com/interactive/2019/08/08/opinion/sunday/party-polarization-quiz.html), "Let Us Predict Whether
You’re a Democrat or a Republican." The survey goes through a series of social, seemingly non-politically inclined questions to determine the political party of the end user.

## About
This program is developed as part of a class project (94-806: [Privacy in the Digital Age](https://api.heinz.cmu.edu/courses_api/course_detail/94-806/), Carnegie Mellon University - [Heinz College](https://www.heinz.cmu.edu/), [Dr. Alessandro Acquisti](https://www.heinz.cmu.edu/~acquisti/).

## Usage
To use this program

1. Clone the repo onto your machine locally:
 - SSH: `git clone git@github.com:rachaelharris/partyguesser.git`
 - HTTPS: `git clone git@github.com:rachaelharris/partyguesser.git`

2. Navigate to the project directory:
`cd partyguesser/`

3. Run the program
   `python3 guesser.py`

4. Analyze the results
   - Open the file `results.csv` in your text editor of choice
   - Suggested analysis: open with RStudio to run regressions on the data to predict results for larger sample sets
   - Suggested analysis: open with Tableau to visualize the data you have collected
  


## FAQ: 
- Q: Will user's information be collected as part of the survey?
- A: No. Their answers will be recorded, but nothing about their identity (i.e., name, phone number, email is not recorded)

- Q: How will the results be used?
- A: The results are intended to be used as part of a class project to demonstrate how seemingly unrelated information can be used to generate profiles about individuals. 


## Contact
For any inquiries, please contact:
 - Rachael Harris (rharris2@andrew.cmu.edu)
 - Morgan Douglas (madougla@andrew.cmu.edu)
 - Tyson Lindley (tlindley@andrew.cmu.edu)
 - Andy Strozewski (astrozew@andrew.cmu.edu)
