The file DNA.txt is a portion of the human genomic sequence, and is
the database in which keywords need to be found.

The files queries.txt and queries2.txt are dictionaries. Each line in
the files is a distinct keyword. A 'match' refers to an exact match
(no mismatches or indels) of the entire keyword to a sub-string of the
database.

You must search both dictionaries:queries.txt and queries2.txt. For
each keyword in queries.txt and queries2.txt, you must report the number of matches found. For the
smaller file queries.txt, you must comment on whether the number of
matches is less than what you expected, more, or about the same. Here,
the expected value is based upon an E-value calculation.