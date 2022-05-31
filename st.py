import streamlit as st
import BP2

bp = BP2.BP_Updater()


# def onClickUpdate():
#     st.write('Values:', values)
#     bp.update(values[0], values[1])

def onClickUpdate():
    st.write('Dabase is updating...')
    bp.update(starting_row, ending_row)


st.title('BP Database Updater')

starting_row = st.number_input('Insert starting row number', min_value=2, help='You need to starting row of your database table')
ending_row = st.number_input('Insert ending row number', max_value=3000)

# values = st.slider(
#      'Select a range',
#      2, 100, (2, 100), step=1)


updateButton = st.button('Update Date', on_click=onClickUpdate)
