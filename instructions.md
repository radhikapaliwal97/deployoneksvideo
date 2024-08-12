# ITV Content Technology Python Coding Exercise Instructions

Thank you for investing time in our coding exercise, good luck and remember to
commit often.

While the full exercise is provided, if you do not have time to complete the full solution,
please select one of the two acceptance criteria and submit a partial solution instead.

This should enable you to demonstrate good engineering practices with a smaller time
investment. If doing so, please make this clear in the submission readme.

Please submit your solution within a week. If you need longer, please get in touch with
the recruiter.

## Requirements

The ITV Hub displays thumbnail images to give viewers a taste of what each show
is about.

In this exercise, you are going to build an application that is meant to generate
a thumbnail for a piece of content. The application should:

1. Verify that the downloaded video has not been corrupted
2. Create a thumbnail from the downloaded video file

The point in the video from which to capture the thumbnail should be provided as
an argument to the service along with the asset_id. Some of the solution has been
completed for you.

Sample content (video assets) can be downloaded from the following endpoint:

`https://cdfr062ui5.execute-api.eu-west-1.amazonaws.com/playground/${assetId}`

An associated metadata endpoint provides the expected checksum for
each asset:

`https://cdfr062ui5.execute-api.eu-west-1.amazonaws.com/playground/${assetId}/metadata`

Verification involves checking that the checksum of the file matches an
expected checksum exposed by the `/metadata` endpoint above.

In order to test your solution, some files have been provided in the repository. 
Example content and metadata have been uploaded to the API. You can access this
by replacing `assetId` with `valid` and `invalid`, for testing success and error
conditions respectively.

A command-line application is desired. The main.py file at the root has been
configured to handle the command line arguments for you and serve as the entry
point for the program. 

A package called thumbnail, a tests directory and a few additional files have been
supplied which you may optionally choose to use at your discretion.

## Hints

To cut down the time spent, there is no need for the service to download files
automatically. Providing a path to a local video file is fine.  You can use any
tool you like to generate thumbnails, but we would recommend ffmpeg, an open source
tool that can be called as follows:

`ffmpeg -ss 00:00:5 -i source_video.mp4 -frames:v 1 -update true thumbnail.png`

## Submitting your solution

Please submit your solution in this Github repository.

To let us know you are ready for your submission to be reviewed, please either
open a github issue or communicate via your recruiter.

Your solution should include a README.md file that contains any assumptions,
design decisions or instructions for running the code.  Please don’t spend more
than a few hours on this exercise. We are looking for evidence of good engineering
practices rather than a fully-polished implementation.

If you have any questions about this exercise, issues are enabled on the Github repo,
use these for any queries or clarification required. We will aim to respond to these
within business hours and don't consider any question to be silly.
