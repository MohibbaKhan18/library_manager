import streamlit as st


if "library" not in st.session_state:
    st.session_state.library = []  #session_state only saves data temporarily and will restart after refreshing the window

library = st.session_state.library

st.title("Your Own Library Manager")

opt1, opt2, opt3, opt4, opt5 = st.tabs(["Add Book", "Search", "View All", "Stats", "Remove"])

#Add Book Option
with opt1:
    st.subheader("Add a New Book")
    with st.form("add_book_form"):
        title = st.text_input("Title")
        author = st.text_input("Author")
        year = st.number_input("Publication Year")
        genre = st.text_input("Genre")
        read = st.checkbox("Read")
        submitted = st.form_submit_button("Add Book")

        if submitted:
            book = {
                "title": title,
                "author": author,
                "year": int(year),
                "genre": genre,
                "read": read
            }
            library.append(book)
            st.success(f"'{title}' added to your library!")

#Search Option
with opt2:
    st.subheader("Search by Title or Author")
    query = st.text_input("Enter search term").lower()
    if query:
        results = [book for book in library if query in book['title'].lower() or query in book['author'].lower()]
        if results:
            st.write(f"Found {len(results)} result(s):")
            st.dataframe(results)
        else:
            st.warning("No matching books found.")

#View All Option
with opt3:
    st.subheader("View All Books")
    if library:
        st.dataframe(library)
    else:
        st.info("Library is currently empty.")

#Statistics Option
with opt4:
    st.subheader("Library Statistics")
    total_books = len(library)
    read_books = sum(1 for book in library if book['read'])
    if total_books:
        read_percent = (read_books / total_books) * 100
        st.metric("Total Books", total_books)
        st.metric("Books Read", f"{read_books} ({read_percent:.1f}%)")
    else:
        st.info("No books in your library yet.")

#Remove Book Option
with opt5:
    st.subheader("Remove a Book")
    if library:
        book_titles = [book['title'] for book in library]
        selected_title = st.selectbox("Select a book to remove", book_titles)
        if st.button("Remove Book"):
            st.session_state.library = [book for book in library if book['title'] != selected_title]
            st.success(f"'{selected_title}' Book has been removed.")
    else:
        st.info("Nothing to remove — your library is empty!")

st.write("")