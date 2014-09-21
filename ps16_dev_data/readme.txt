The data has transcripts of voice recordings from an experiment which involved 6 subjects (all male) performing educationally-related tasks, while they were being eye-tracked. There were four tasks:

1. A usability-related task in which the subject responds to questions about the MyCourses software; the questions were asked by the facilitator
2. A cooperative game task in which the subject was expected to give instructions to the facilitator as they played the game together
3. An image interpreting task in which the subject responded to the facilitators’ questions about factual (material) and social-emotional information in the images
4. A Math/Tutoring task where the subject responded to questions asked by the facilitator, aiming at tutoring her.

The voice recording has been transcribed verbatim in upper case only with a few special symbols used to indicate speech phenomena (e.g., {SL} indicates a silent pause and {NS} indicates background noise). They were then subject to automatic forced alignment to the speech (mistakes might occur) which is what you see in the Praat TextGrids.

A facilitator (female) was present (asking questions, etc.) and the microphone recorded both the subject and the facilitator. Generally, the subject speaks more than the facilitator, but there are some parts where the experimenter is speaking more(e.g., explaining eye-tracking or experimental procedures at beginning or end). 

You receive two sets of files per transcript:

 AS2_T1_Stereo.TextGrid | the time-aligned Praat transcripts and annotation (by question)
 AS2_T1_Stereo.txt      | the plain-text transcription, usually running text

You should download Praat from praat.org which allows you to visualize the TextGrid file. You can also open the TextGrid file in a text editor, and treat it as plain text. Additional information (e.g. start and end times) are also included in its format.

Your job is to try to creatively segment utterances based on the plain text file, and assign them to each speaker.

For subject AS1, you receive two TextGrid files where the speakers have been separated. 
We will compare your program’s output with two similar TextGrid files. We have held out these files for evaluation: 

    AS1_T2_Stereo
    AS1_T3_Stereo

== NAMING CONVENTION ===========================================================

The files are named [subj]_[task]_[Fac/Sub/Stereo]:

e.g. AS1_T1_Fac =
		  [AS1] subject id (group 1)
		  [T1]  task #1
		  [Fac] facilitator's mic audio

e.g. TD2_T3_Sub =
		  [TD2] subject id (group 2)
		  [T3]  task #3
		  [Sub] subject's mic audio


== TEXTGRIDS ===================================================================

Each Praat TextGrid file has four tiers:

#     | NAME        | DESCRIPTION
[0] 1 | phone       | Arpabet sound phones (by automatic forced alignment)
[1] 2 | participant | Participant's transcript (transcribed manually)
[2] 3 | facilitator | Facilitator's transcript moved here for AS1_T1_Stereo, AS1_T4_Stereo
[3] 4 | task        | Task information [for most subjects, tasks]


Task information on tier 4:

    mycourses_q# | e.g. mycourses_q1 | the first question
                  
 
    images_n#_q# | e.g. images_n1_q1 | the first image [n#], first question [q#]
                  

    math_n#_q#   | e.g. math_n1_q1 0/5 | first image [n#], first question [q#]

