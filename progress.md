Oct 8: Rebuilt MST UI from scratch, no AI. 4 sliders in variables, st.button, 
CSV append with f-string. Learned: check docs for function names, 
quotes around filenames, "a" mode appends.
Next: header row once, \n at end, 7-day average, validation.

Oct 9: Got header-once logic working in concept: os.path.exists(file_name),
",".join(header) for header row, "w" to create and "a" to append. Added
DateTime column. Struggled with: else lined up with the button's if instead
of the file check (Streamlit reruns the script on every slider move, so that
spams rows), and too many nested with blocks. Learned: write() takes one
string only, \n goes at the END of a row, never hardcode the filename twice.
Next: delete the else + extra with blocks, test with 2 submits (expect 1
header, 2 rows). Then: read CSV back, 7-day average, validation.