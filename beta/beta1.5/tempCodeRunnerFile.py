    curr.execute("""
            SELECT username,
            pgp_sym_decrypt(
                password,
                pgp_sym_decrypt(encrypted_key, %s::text)
            )
            FROM users
            WHERE websit