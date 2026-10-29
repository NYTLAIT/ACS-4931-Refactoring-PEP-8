# by Kami Bigdely
# Indentation

######################
# Consider the following guidelines:

# - Use 4 spaces per indentation level.
# - Maximum line length is 79 characters.
# - Continuation lines should align wrapped elements either vertically 
# using Python's implicit line joining inside parentheses, brackets and braces, 
# or using a hanging indent. Refer to class slides for visual explanation.
######################

def write_to_db():
   print('person info are written into db.')
    
    
def set_person_info(
        first_name, last_name, gender, date_of_birth, photo, nationality, place_of_birth
    ):

    if not first_name:
        print('first name is empty.') 
    if not last_name:
        print('last name is empty.')
    # ...    
    write_to_db()

photo_path = "https://en.wikipedia.org/wiki/Tim_Hunt#/media/File:Tim_Hunt_at_UCSF_05_2009_(4).jpg"
set_person_info(
    'Tim', 
    'Hunt', 
    'male',
    '19 February 1943', 
    photo_path, 
    'Uited Kingdom', 
    'Neston, Cheshire, England'
)

######################
# NOTE: CHOICE of leaving link as one is more practical and pep 8 approved
# SAUCE: https://peps.python.org/pep-0008/#indentation
#
# NOTE: Types approved by PEP 8 (all are 'implicit' and what is prefered)
#
# - Vertical alignment (first line argument fine but all below should line up to that argument)
# - Hanging indent (example used set_person_info, no argument on function call line)
# - 8-Space (hanging indent but on one line only after function name indented 8 spaces 
# instead of 4, example on set_person_info)
#
# NOTE: Few more tips
# - Explicit Backslash
# with open('/path/to/some/file/you/want/to/read') as file_1, \
#      open('/path/to/some/file/being/written', 'w') as file_2:
#     file_2.write(file_1.read())
######################