from tools.tools import *
import multiprocessing

"""
if __name__ == "__main__":
    webpages = ["https://www.magneto365.com/co/empleos",'https://example.com', "https://co.computrabajo.com/"]
    with multiprocessing.Pool() as pool:

        results = pool.map(crawl, webpages)

    print(results)
"""
crawl('https://www.magneto365.com/co/empleos')



"""
<div class="mg_jobs_page_magneto-ui-jobs-page--center-row_jobs-result_18fvy"><article class="mg_job_card_mobile_magneto-ui-card-mobile-jobs_18tcb  undefined"><div class="mg_job_card_mobile_magneto-ui-card-mobile-jobs--row1_18tcb"><div class="mg_job_card_mobile_magneto-ui-card-mobile-jobs--brand_18tcb"><img class="mg_job_card_mobile_magneto-ui-card-mobile-jobs--brand_img_18tcb" alt="jeronimo-martins" src="https://media.magneto365.com/image_assets/files/17689/original-376bc294-0b76-483e-b2d8-9df008f6593b-.png?Expires=1715299199&amp;Key-Pair-Id=KYGE9B84R3EDO&amp;Signature=SuFUKstOX6Sneq4q~0lirxm4wDUPCTtFtjjpC9pYTzLFbsmAsSQ60log-S-rF8An8zFl1BtQIbB0hnv~Ru4IPPQDg1BhVZyr3WWuB8ac10iBGylFgw5u~Znfwa8jtu81hW0lLSd3LrDED6jMLSmJwXetETD6TPB2PSpTPXWSMh2qXMhDrYUcESXDe-sCoeulpn771cuYUYOsGjyqVtqRjtrkk5JUlZGjO9q0ogYrTfsGyNfI0AcZtYGorxaoa0S2mBdpC2VOBQi1SZVOCedMvaXkefvZIomS3tnKNhhOVMxOWCqjiwxHUtwvf8q54qlOb7gHeADNWOsIAxvmhHAw9Q__" loading="lazy" width="50px" height="50px"></div></div><div class="mg_job_card_mobile_magneto-ui-card-mobile-jobs--data_18tcb"><div class="mg_job_card_mobile_magneto-ui-card-mobile-jobs--row2_18tcb"><div><a href="https://www.magneto365.com/co/empleos/jefe-de-tienda-tiendas-ara-palmira-valle-del-cauca-01434c97-db8b-4d60-8c32-1614c4196bc1" title="Jefe De Tienda - Tiendas Ara - Palmira-Valle del cauca" rel="noreferrer"><h2 class="mg_job_card_mobile_magneto-ui-card-mobile-jobs--row2_position_18tcb ">Jefe De Tienda - Tiendas Ara - Palmira-Valle del cauca</h2></a></div><div class="mg_job_card_mobile_magneto-ui-card-mobile-jobs--row2_info_18tcb"><h3>Ara,</h3><p>Hace  5 horas,</p><p>Cali - El Cerrito - Palmira  </p><p>$&nbsp;2.801.000, </p><p>2 años de experiencia,  </p><p>Bachillerato completo, Técnico, Tecnólogo, Profesional.</p></div></div></div></article><article class="mg_job_card_mobile_magneto-ui-card-mobile-jobs_18tcb  "><div class="mg_job_card_mobile_magneto-ui-card-mobile-jobs--row1_18tcb"><div class="mg_job_card_mobile_magneto-ui-card-mobile-jobs--brand_18tcb"><img class="mg_job_card_mobile_magneto-ui-card-mobile-jobs--brand_img_18tcb" alt="levapan" src="https://media.magneto365.com/image_assets/files/62293/original-e5575c67-d2c3-4d48-9823-f2e1831c121b-.png?Expires=1715299199&amp;Key-Pair-Id=KYGE9B84R3EDO&amp;Signature=VajoEt3L0KQF56r3YzDoEZQervWl9AB-TrAbjwrKE~GJC--hvFtr0W1my220Wdrwxj0RuxigkeUzlEwB2YZtSS0IHp9BG7-KzEODVM-~-daTE2r86~CWa~ckwGjMHBU0dswLpiaJmJo6Jc8XjVkaZpZVuTE7geol2H0O7IuZLmapHP5MZ6wFRIZDd1Ngw-HWN9UrG0TniQvNKLLsh-T31LA9UCcYgg2M0PjDqi6ykRsRTsU9vWhngksa9GoHernk~0PB1FNtRk1-XPNq5u772Oi8WpcZ~aVVAMgR8yI8PhF6-wme5pnNANuOZ3LOqyiRWl9Sb5Wu-hiWUQnLY7vWSA__" loading="lazy" width="50px" height="50px"></div></div><div class="mg_job_card_mobile_magneto-ui-card-mobile-jobs--data_18tcb"><div class="mg_job_card_mobile_magneto-ui-card-mobile-jobs--row2_18tcb"><div><a href="https://www.magneto365.com/co/empleos/aprendices-t-cnicos-tecn-logos-planta-tulu-4d8b5d3a-ecd4-4806-b9b2-4fd0716112c9" title="Aprendices Técnicos, Tecnólogos Planta Tuluá" rel="noreferrer"><h2 class="mg_job_card_mobile_magneto-ui-card-mobile-jobs--row2_position_18tcb ">Aprendices Técnicos, Tecnólogos Planta Tuluá</h2></a></div><div class="mg_job_card_mobile_magneto-ui-card-mobile-jobs--row2_info_18tcb"><h3>Grupo Levapan,</h3><p>Hace  5 horas,</p><p>Tuluá  </p><p>Salario a convenir, </p><p> </p><p>Técnico, Tecnólogo.</p></div></div></div></article><article class="mg_job_card_mobile_magneto-ui-card-mobile-jobs_18tcb  "><div class="mg_job_card_mobile_magneto-ui-card-mobile-jobs--row1_18tcb"><div class="mg_job_card_mobile_magneto-ui-card-mobile-jobs--brand_18tcb"><img class="mg_job_card_mobile_magneto-ui-card-mobile-jobs--brand_img_18tcb" alt="solvo" src="https://media.magneto365.com/image_assets/files/11822/original-logo-.png?Expires=1715299199&amp;Key-Pair-Id=KYGE9B84R3EDO&amp;Signature=bdRYAQ6DRi3Za-xTTiWAjZ6FXrtD9jFxg9BJCOQpcD4isvsgCPLrVNTtoYI2KepvwiSrK~z2idvq-0C9Af0XS846qpvIwBXT6dDJH3BBJP~3pf1-~bNIcRy4b-vKTddQaXstruBNM3cDWPz1hx5NkHkKg0ewEX9m5xdjP7byuXoQwUSGCav7h8StX3AhigIChHiItXKT5sLBDl1O1m7KK7bFR~oMsPFBmhWDtymyAvHswfWoY7tNRIcdQ5lNqA8sDg3MyIMLdZSoTF-kmxfxVQpgXrwR70dHKQxLZm8TbgTe~OE-YM5pUi8CUIKkz642EApstcWoM5ypun0XWNtIWA__" loading="lazy" width="50px" height="50px"></div></div><div class="mg_job_card_mobile_magneto-ui-card-mobile-jobs--data_18tcb"><div class="mg_job_card_mobile_magneto-ui-card-mobile-jobs--row2_18tcb"><div><a href="https://www.magneto365.com/co/empleos/data-entry-7afeb3a2-6ff3-4414-a172-8e69570919c2" title="Data Entry" rel="noreferrer"><h2 class="mg_job_card_mobile_magneto-ui-card-mobile-jobs--row2_position_18tcb ">Data Entry</h2></a></div><div class="mg_job_card_mobile_magneto-ui-card-mobile-jobs--row2_info_18tcb"><h3>Solvo Global,</h3><p>Hace  5 horas,</p><p>Cali  </p><p>$&nbsp;2.600.000, </p><p>6 meses de experiencia,  </p><p>Bachillerato completo.</p></div></div></div></article><article class="mg_job_card_mobile_magneto-ui-card-mobile-jobs_18tcb  "><div class="mg_job_card_mobile_magneto-ui-card-mobile-jobs--row1_18tcb"><div class="mg_job_card_mobile_magneto-ui-card-mobile-jobs--brand_18tcb"><img class="mg_job_card_mobile_magneto-ui-card-mobile-jobs--brand_img_18tcb" alt="zentria" src="https://media.magneto365.com/image_assets/files/22981/original-d641dc5e-a8aa-4812-821a-ce0d9335fc7b-.png?Expires=1715299199&amp;Key-Pair-Id=KYGE9B84R3EDO&amp;Signature=nyGpd6aXVgnjcKtzoBrx5annGSgnkgZKoG3Bi-O3-iimo4f59RlaqzfiQMqUh0mceHPmkFPN-S7tQKqWJUrYu5frV~Lh0OzHoCk854LVlXXbLD34obUFQ9XbvF3JABsmNL9M9aZJT7398j2NwM5UCdfhakC6AXkfB4cL2GCg5WkZXdgEbzfO9FV6WZvVPZkfBUkdTf-2YeQ~SBoCkYXfwXdQhsQruXjFZ66R4HlX4BFjNemfXUsL39yzTGemNgmGQ8h7TLySPmCN7KagCwzZ4EPsDty0LmLoKY15gLe8C3GKOX4Q1SHmkN1A2ohm3mGqXt4AgIYA-9cq-l6OXJOwgA__" loading="lazy" width="50px" height="50px"></div></div><div class="mg_job_card_mobile_magneto-ui-card-mobile-jobs--data_18tcb"><div class="mg_job_card_mobile_magneto-ui-card-mobile-jobs--row2_18tcb"><div><a href="https://www.magneto365.com/co/empleos/auxiliar-siau-191ac856-0b8d-49fa-83a4-23669bf9f7de" title="Auxiliar Siau" rel="noreferrer"><h2 class="mg_job_card_mobile_magneto-ui-card-mobile-jobs--row2_position_18tcb ">Auxiliar Siau</h2></a></div><div class="mg_job_card_mobile_magneto-ui-card-mobile-jobs--row2_info_18tcb"><h3>Zentria,</h3><p>Hace  5 horas,</p><p>Manizales  </p><p>$&nbsp;1.478.000, </p><p>1 año de experiencia,  </p><p>Técnico, Tecnólogo.</p></div></div></div></article><article class="mg_job_card_mobile_magneto-ui-card-mobile-jobs_18tcb  "><div class="mg_job_card_mobile_magneto-ui-card-mobile-jobs--row1_18tcb"><div class="mg_job_card_mobile_magneto-ui-card-mobile-jobs--brand_18tcb"><img class="mg_job_card_mobile_magneto-ui-card-mobile-jobs--brand_img_18tcb" alt="colsubsidio-empleo" src="https://media.magneto365.com/image_assets/files/8477/original-logo-header-agencia-de-empleo2-.jpg?Expires=1715299199&amp;Key-Pair-Id=KYGE9B84R3EDO&amp;Signature=js-IKsCFNCkFrGKNgg-m4ZXvw3PM-QZqRlk0zJ0lSIYYLrBRnvlLaWOMVSE6DjUnWsnENd3uF~fnfHXlTd9RJr9HWh5M2K2XKoIPXLmsNDPJRTLSVNp93WIiw1cvQpyksX5Yq85mlYqxXcTqgQAX2eM0IprPNVUbYoMrrrludVfbWQ~udGwBlasPTp7M1yuNl~eUj9A-JzNXwA2geqDpsvrvQE-VAgFobvWG8l9CiykTpHvBzys2X7Uqk~ps4lnjn1lbI-DtbTILZtwwtLT2EbNRHhotjQVXS50KJjp39hB2pkIN6TyH9u0CpmCZH2DypsyJoKDKIzMQyXJgX7T-kg__" loading="lazy" width="50px" height="50px"></div></div><div class="mg_job_card_mobile_magneto-ui-card-mobile-jobs--data_18tcb"><div class="mg_job_card_mobile_magneto-ui-card-mobile-jobs--row2_18tcb"><div><a href="https://www.magneto365.com/co/empleos/convocatoria-laboral-asesores-comerciales-tiempo-completo-o-fds-bogot-norte-69c77ad1-7a08-4a47-abf0-d65cdde0aad2" title="Convocatoria Laboral Asesores Comerciales Tiempo Completo o FDS Bogotá Norte" rel="noreferrer"><h2 class="mg_job_card_mobile_magneto-ui-card-mobile-jobs--row2_position_18tcb ">Convocatoria Laboral Asesores Comerciales Tiempo Completo o FDS Bogotá Norte</h2></a></div><div class="mg_job_card_mobile_magneto-ui-card-mobile-jobs--row2_info_18tcb"><h3>Colsubsidio Empleo,</h3><p>Hace  5 horas,</p><p>Bogotá, D.C.  </p><p>$&nbsp;1.300.000, </p><p>3 meses de experiencia,  </p><p>Bachillerato completo, Técnico, Tecnólogo.</p></div></div></div></article><article class="mg_job_card_mobile_magneto-ui-card-mobile-jobs_18tcb  "><div class="mg_job_card_mobile_magneto-ui-card-mobile-jobs--row1_18tcb"><div class="mg_job_card_mobile_magneto-ui-card-mobile-jobs--brand_18tcb"><img class="mg_job_card_mobile_magneto-ui-card-mobile-jobs--brand_img_18tcb" alt="aris-mining" src="https://media.magneto365.com/image_assets/files/51863/original-7248290d-9835-4e77-9c1f-02d4b20df77a-.png?Expires=1715299199&amp;Key-Pair-Id=KYGE9B84R3EDO&amp;Signature=TOjs-p8S5RjikDyrZrnG5eQjODl1~lcPrFuxnPtvYs0CzshSfcT6MSIkRNaL35eR78uc0rsPsG5dchiwO7BB8kp6zCBeQ2QOE5U~BVepHm24B4xc48Xf8AJzbkL2wOGY-qrpUgEXlcHAW8dQgxA8~REH6QwUzPL~~cuQ8I5O5XRm9O8zhCbH92dXqMC0tBvfS2D-~AVggjtRbqHfqRNIAXwPtrJj6VDqQHJI~P9udGFY-~2DiJgQcuS-qCEzUGIUeqRD3UV2df3vhkGyahv~8hXu5mPP1uk3JroX9VnNHv1K4i8pcj3lSidID089hk280XWEUeiOaEIU1Mq3uZD3Lw__" loading="lazy" width="50px" height="50px"></div></div><div class="mg_job_card_mobile_magneto-ui-card-mobile-jobs--data_18tcb"><div class="mg_job_card_mobile_magneto-ui-card-mobile-jobs--row2_18tcb"><div><a href="https://www.magneto365.com/co/empleos/practicante-universitario-derecho-0718ba4f-6b70-4f18-a3db-a29478e457cd" title="Practicante Universitario Derecho" rel="noreferrer"><h2 class="mg_job_card_mobile_magneto-ui-card-mobile-jobs--row2_position_18tcb ">Practicante Universitario Derecho</h2></a></div><div class="mg_job_card_mobile_magneto-ui-card-mobile-jobs--row2_info_18tcb"><h3>ARIS MINING,</h3><p>Hace  5 horas,</p><p>Marmato  </p><p>$&nbsp;1.300.000, </p><p> </p><p>Bachillerato (grados 9°, 10° y 11°).</p></div></div></div></article><article class="mg_job_card_mobile_magneto-ui-card-mobile-jobs_18tcb  "><div class="mg_job_card_mobile_magneto-ui-card-mobile-jobs--row1_18tcb"><div class="mg_job_card_mobile_magneto-ui-card-mobile-jobs--brand_18tcb"><img class="mg_job_card_mobile_magneto-ui-card-mobile-jobs--brand_img_18tcb" alt="magneto-pymes" src="https://media.magneto365.com/image_assets/files/61449/original-31b99585-8a5b-4e01-b307-9bc5d622d0d1-.jpeg?Expires=1715299199&amp;Key-Pair-Id=KYGE9B84R3EDO&amp;Signature=gwJ5-C0bi9gf2amK2PVW1Ulw7DIs2KElj5QtZPZiVS9su6KXPhK8-bTFROnMMJOSi-k2UMJeIq1vRCRPZBD9rx0eqszvqxK0VN1FXj0E~29bGsBxz95IUruatLyDOqnd9Z5gh4p2mCt6o2f6LPaAabgHpVUrqhbAcNjW2YwRqCcTBIH7u8IYr0OuzvQDXYGZoHZf8IgPPx4PdNwaKxJ4GBsPyP5dFHIgJuFHpQAG0sVDBH74djmg5P4Vc0-EDG6rRh8by74DoQQfOTcVKsz1MIl9XDvfPfTnGEh9CB6x3syd1NRTFEIHULyYC9o2NyCNg1h~u7RMgrBE2LyN1mEFXA__" loading="lazy" width="50px" height="50px"></div></div><div class="mg_job_card_mobile_magneto-ui-card-mobile-jobs--data_18tcb"><div class="mg_job_card_mobile_magneto-ui-card-mobile-jobs--row2_18tcb"><div><a href="https://www.magneto365.com/co/empleos/gerente-general-c1bed4d9-cebb-45ff-a513-9670713d02d3" title="GERENTE GENERAL" rel="noreferrer"><h2 class="mg_job_card_mobile_magneto-ui-card-mobile-jobs--row2_position_18tcb ">GERENTE GENERAL</h2></a></div><div class="mg_job_card_mobile_magneto-ui-card-mobile-jobs--row2_info_18tcb"><h3>TALENTO EXTREMO SAS,</h3><p>Hace  5 horas,</p><p>Armenia  </p><p>$&nbsp;16.900.000, </p><p>5 años de experiencia,  </p><p>Profesional, Especialización/ Maestría, Doctorado.</p></div></div></div></article><article class="mg_job_card_mobile_magneto-ui-card-mobile-jobs_18tcb  "><div class="mg_job_card_mobile_magneto-ui-card-mobile-jobs--row1_18tcb"><div class="mg_job_card_mobile_magneto-ui-card-mobile-jobs--brand_18tcb"><img class="mg_job_card_mobile_magneto-ui-card-mobile-jobs--brand_img_18tcb" alt="team" src="https://media.magneto365.com/image_assets/files/7303/original-logo-.jpg?Expires=1715299199&amp;Key-Pair-Id=KYGE9B84R3EDO&amp;Signature=HumlMz4RwPBs7s~HM4CHIxZdsA~kg3K0r1XSpw~g5~9CKOUyPCVX6YrNpS7oTiIOWiCLoOkiPeU~Br39XtW0kYyiAR1GSjGcVscrdC8PzGu5dHwhzd-y-M9KoEvP2IhExSnS8ItqSBT77bXMm5VuxqEo-Hh5UMpZKZcZbcLIBYc1BR2Q2MAuNU052aoO4GXjTOBXCmw5Ie2hs88SxqcpLlAtXi5vhAbM3oG-IydDnHHjtlZ4g9qiFjsWnDbouyhrBoxH-Z-XSh0zLh55uv9VexeqdBLfrgu-oijj5UlMwPlNSl0HocCaZE~xXE~6ic-46p6urgarZcOaue5ue7PT6A__" loading="lazy" width="50px" height="50px"></div></div><div class="mg_job_card_mobile_magneto-ui-card-mobile-jobs--data_18tcb"><div class="mg_job_card_mobile_magneto-ui-card-mobile-jobs--row2_18tcb"><div><a href="https://www.magneto365.com/co/empleos/sustainability-analyst-0fa46a7a-0210-4465-a18e-a911dda0a266" title="Sustainability and Data Analyst" rel="noreferrer"><h2 class="mg_job_card_mobile_magneto-ui-card-mobile-jobs--row2_position_18tcb ">Sustainability and Data Analyst</h2></a></div><div class="mg_job_card_mobile_magneto-ui-card-mobile-jobs--row2_info_18tcb"><h3>Alianza Team,</h3><p>Hace  5 horas,</p><p>Otra (Bogotá D.C.) - Bogotá, D.C.  </p><p>$&nbsp;3.000.000 a $&nbsp;4.500.000, </p><p>1 año de experiencia,  </p><p>Profesional, Especialización/ Maestría.</p></div></div></div></article><article class="mg_job_card_mobile_magneto-ui-card-mobile-jobs_18tcb  "><div class="mg_job_card_mobile_magneto-ui-card-mobile-jobs--row1_18tcb"><div class="mg_job_card_mobile_magneto-ui-card-mobile-jobs--brand_18tcb"><img class="mg_job_card_mobile_magneto-ui-card-mobile-jobs--brand_img_18tcb" alt="semana" src="https://media.magneto365.com/image_assets/files/44562/original-2339f413-0fcf-49e9-aa78-2381ae285d1b-.jpeg?Expires=1715299199&amp;Key-Pair-Id=KYGE9B84R3EDO&amp;Signature=L6z0ASoT0AuYH9P2npv7QOV8JRLtaL3lBkiyj6VsUt~ZRXZDbieFl3yknYtEz8PL0sLw2HwHBIyNo4LYSxifALc6od2AZXSMCMm1fGHw3O0otHs-K-CTA-t5t~blID4HPxz8j6jE59FGLXZi2f-BJmPIoa2D~0g6cFshhaFcTABfCiMZMQs36CZDKQ1sAy2Esm0HsTlyhM0wvXTgrpm8i9sI-sbDFCnHVMYIbW3qbPp3nIo0TlC3kO4AO4GGCj-KJoIMjl1GfXkuoXegSScw99fFVABEjbr7xFHFu1DYspApf7vHHY5ak9tKX1c-tKKJps5zTYu5xJCIcC8eSZ8aVw__" loading="lazy" width="50px" height="50px"></div></div><div class="mg_job_card_mobile_magneto-ui-card-mobile-jobs--data_18tcb"><div class="mg_job_card_mobile_magneto-ui-card-mobile-jobs--row2_18tcb"><div><a href="https://www.magneto365.com/co/empleos/analista-contable-bogot-a53f9dd5-f2cc-4590-ba52-1d5d37105164" title="Analista contable - Bogotá" rel="noreferrer"><h2 class="mg_job_card_mobile_magneto-ui-card-mobile-jobs--row2_position_18tcb ">Analista contable - Bogotá</h2></a></div><div class="mg_job_card_mobile_magneto-ui-card-mobile-jobs--row2_info_18tcb"><h3>Semana,</h3><p>Hace  5 horas,</p><p>Otra (Bogotá D.C.)  </p><p>$&nbsp;2.180.000, </p><p>3 años de experiencia,  </p><p>Tecnólogo, Profesional.</p></div></div></div></article><article class="mg_job_card_mobile_magneto-ui-card-mobile-jobs_18tcb  "><div class="mg_job_card_mobile_magneto-ui-card-mobile-jobs--row1_18tcb"><div class="mg_job_card_mobile_magneto-ui-card-mobile-jobs--brand_18tcb"><img class="mg_job_card_mobile_magneto-ui-card-mobile-jobs--brand_img_18tcb" alt="magneto" src="https://static.magneto365.com/meta/confidencial.svg" loading="lazy" width="50px" height="50px"></div></div><div class="mg_job_card_mobile_magneto-ui-card-mobile-jobs--data_18tcb"><div class="mg_job_card_mobile_magneto-ui-card-mobile-jobs--row2_18tcb"><div><a href="https://www.magneto365.com/co/empleos/l-der-tat-aliados-comerciales-manizales-77388ff7-2018-4aed-9522-6767556be491" title="Líder TAT Aliados Comerciales - Manizales" rel="noreferrer"><h2 class="mg_job_card_mobile_magneto-ui-card-mobile-jobs--row2_position_18tcb ">Líder TAT Aliados Comerciales - Manizales</h2></a></div><div class="mg_job_card_mobile_magneto-ui-card-mobile-jobs--row2_info_18tcb"><h3>Confidencial,</h3><p>Hace  5 horas,</p><p>Otra (Quindio) - Otra (Caldas) - Manizales - Armenia  </p><p>$&nbsp;3.500.000 a $&nbsp;4.850.000, </p><p>1 año de experiencia,  </p><p>Técnico, Tecnólogo, Profesional, Especialización/ Maestría.</p></div></div></div></article><article class="mg_job_card_mobile_magneto-ui-card-mobile-jobs_18tcb  "><div class="mg_job_card_mobile_magneto-ui-card-mobile-jobs--row1_18tcb"><div class="mg_job_card_mobile_magneto-ui-card-mobile-jobs--brand_18tcb"><img class="mg_job_card_mobile_magneto-ui-card-mobile-jobs--brand_img_18tcb" alt="colsubsidio-talento-humano" src="https://media.magneto365.com/image_assets/files/31952/original-49d58b9f-156f-4fca-8c1e-83e351b81941-.png?Expires=1715299199&amp;Key-Pair-Id=KYGE9B84R3EDO&amp;Signature=JDGUgPExsaJGIlTa3enuS72rGuZ0gfqzYq0i0sVVjaZxBmfOqLheWXkIQue1PXM4-kNVxkLsWVK25SMuEmSHjDTvhloszcqwpn~OeXWcxxBgVO7I086KTa8yNoypcPcAd2-3R9BFK4g5~fv0FRSinhaq4rQebiyzFk0yxYsXr9S60wip1ud8~NDLq9-7P50qWEpEGszRlDYmBDJYV~3cPh3WNkIaMI~EhGehnl2W84-I~rA~QXzxPNZPIqpi5IyPfDM3q579a6s2O0bwKoUTum2prbs8qduj55Sw8LAevZkRI5rlxrXm3Zu7C9WiHXS~IhHF-Wf5Zhb7Wi5g5YzAQA__" loading="lazy" width="50px" height="50px"></div></div><div class="mg_job_card_mobile_magneto-ui-card-mobile-jobs--data_18tcb"><div class="mg_job_card_mobile_magneto-ui-card-mobile-jobs--row2_18tcb"><div><a href="https://www.magneto365.com/co/empleos/auxiliar-cocina-42-horas-norte-bogot-c0c69b36-6d97-4312-a76a-f4c1e3d4bf19" title="Auxiliar Cocina 42 horas- Norte Bogotá" rel="noreferrer"><h2 class="mg_job_card_mobile_magneto-ui-card-mobile-jobs--row2_position_18tcb ">Auxiliar Cocina 42 horas- Norte Bogotá</h2></a></div><div class="mg_job_card_mobile_magneto-ui-card-mobile-jobs--row2_info_18tcb"><h3>Colsubsidio Recreación y Deportes,</h3><p>Hace  5 horas,</p><p>Bogotá, D.C.  </p><p>$&nbsp;1.185.000, </p><p>6 meses de experiencia,  </p><p>Bachillerato completo.</p></div></div></div></article><article class="mg_job_card_mobile_magneto-ui-card-mobile-jobs_18tcb  "><div class="mg_job_card_mobile_magneto-ui-card-mobile-jobs--row1_18tcb"><div class="mg_job_card_mobile_magneto-ui-card-mobile-jobs--brand_18tcb"><img class="mg_job_card_mobile_magneto-ui-card-mobile-jobs--brand_img_18tcb" alt="magneto" src="https://static.magneto365.com/meta/confidencial.svg" loading="lazy" width="50px" height="50px"></div></div><div class="mg_job_card_mobile_magneto-ui-card-mobile-jobs--data_18tcb"><div class="mg_job_card_mobile_magneto-ui-card-mobile-jobs--row2_18tcb"><div><a href="https://www.magneto365.com/co/empleos/fonoaudiologa-8cbf48f9-55fe-4d29-8ee7-d08b56d5015f" title="Fonoaudiologa" rel="noreferrer"><h2 class="mg_job_card_mobile_magneto-ui-card-mobile-jobs--row2_position_18tcb ">Fonoaudiologa</h2></a></div><div class="mg_job_card_mobile_magneto-ui-card-mobile-jobs--row2_info_18tcb"><h3>Confidencial,</h3><p>Hace  6 horas,</p><p>Bogotá, D.C.  </p><p>$&nbsp;1.481.189, </p><p>1 año de experiencia,  </p><p>Profesional.</p></div></div></div></article><article class="mg_job_card_mobile_magneto-ui-card-mobile-jobs_18tcb  "><div class="mg_job_card_mobile_magneto-ui-card-mobile-jobs--row1_18tcb"><div class="mg_job_card_mobile_magneto-ui-card-mobile-jobs--brand_18tcb"><img class="mg_job_card_mobile_magneto-ui-card-mobile-jobs--brand_img_18tcb" alt="zentria" src="https://media.magneto365.com/image_assets/files/22981/original-d641dc5e-a8aa-4812-821a-ce0d9335fc7b-.png?Expires=1715299199&amp;Key-Pair-Id=KYGE9B84R3EDO&amp;Signature=nyGpd6aXVgnjcKtzoBrx5annGSgnkgZKoG3Bi-O3-iimo4f59RlaqzfiQMqUh0mceHPmkFPN-S7tQKqWJUrYu5frV~Lh0OzHoCk854LVlXXbLD34obUFQ9XbvF3JABsmNL9M9aZJT7398j2NwM5UCdfhakC6AXkfB4cL2GCg5WkZXdgEbzfO9FV6WZvVPZkfBUkdTf-2YeQ~SBoCkYXfwXdQhsQruXjFZ66R4HlX4BFjNemfXUsL39yzTGemNgmGQ8h7TLySPmCN7KagCwzZ4EPsDty0LmLoKY15gLe8C3GKOX4Q1SHmkN1A2ohm3mGqXt4AgIYA-9cq-l6OXJOwgA__" loading="lazy" width="50px" height="50px"></div></div><div class="mg_job_card_mobile_magneto-ui-card-mobile-jobs--data_18tcb"><div class="mg_job_card_mobile_magneto-ui-card-mobile-jobs--row2_18tcb"><div><a href="https://www.magneto365.com/co/empleos/auxiliar-de-farmacia-735bee55-8d6f-4e5c-b4fb-1a1e5afd82aa" title="Auxiliar de Farmacia" rel="noreferrer"><h2 class="mg_job_card_mobile_magneto-ui-card-mobile-jobs--row2_position_18tcb ">Auxiliar de Farmacia</h2></a></div><div class="mg_job_card_mobile_magneto-ui-card-mobile-jobs--row2_info_18tcb"><h3>Zentria,</h3><p>Hace  6 horas,</p><p>Cali  </p><p>$&nbsp;1.681.000, </p><p>1 año de experiencia,  </p><p>Técnico, Tecnólogo.</p></div></div></div></article><article class="mg_job_card_mobile_magneto-ui-card-mobile-jobs_18tcb  "><div class="mg_job_card_mobile_magneto-ui-card-mobile-jobs--row1_18tcb"><div class="mg_job_card_mobile_magneto-ui-card-mobile-jobs--brand_18tcb"><img class="mg_job_card_mobile_magneto-ui-card-mobile-jobs--brand_img_18tcb" alt="jeronimo-martins" src="https://media.magneto365.com/image_assets/files/17689/original-376bc294-0b76-483e-b2d8-9df008f6593b-.png?Expires=1715299199&amp;Key-Pair-Id=KYGE9B84R3EDO&amp;Signature=SuFUKstOX6Sneq4q~0lirxm4wDUPCTtFtjjpC9pYTzLFbsmAsSQ60log-S-rF8An8zFl1BtQIbB0hnv~Ru4IPPQDg1BhVZyr3WWuB8ac10iBGylFgw5u~Znfwa8jtu81hW0lLSd3LrDED6jMLSmJwXetETD6TPB2PSpTPXWSMh2qXMhDrYUcESXDe-sCoeulpn771cuYUYOsGjyqVtqRjtrkk5JUlZGjO9q0ogYrTfsGyNfI0AcZtYGorxaoa0S2mBdpC2VOBQi1SZVOCedMvaXkefvZIomS3tnKNhhOVMxOWCqjiwxHUtwvf8q54qlOb7gHeADNWOsIAxvmhHAw9Q__" loading="lazy" width="50px" height="50px"></div></div><div class="mg_job_card_mobile_magneto-ui-card-mobile-jobs--data_18tcb"><div class="mg_job_card_mobile_magneto-ui-card-mobile-jobs--row2_18tcb"><div><a href="https://www.magneto365.com/co/empleos/auxiliar-punto-de-venta-florencia-caqueta-90799b7e-4d2f-47e2-972b-fa23f84f4612" title="Auxiliar Punto De Venta - Florencia - Caqueta" rel="noreferrer"><h2 class="mg_job_card_mobile_magneto-ui-card-mobile-jobs--row2_position_18tcb ">Auxiliar Punto De Venta - Florencia - Caqueta</h2></a></div><div class="mg_job_card_mobile_magneto-ui-card-mobile-jobs--row2_info_18tcb"><h3>Ara,</h3><p>Hace  6 horas,</p><p>Florencia  </p><p>$&nbsp;1.300.000, </p><p>6 meses de experiencia,  </p><p>Bachillerato completo, Técnico, Tecnólogo.</p></div></div></div></article><article class="mg_job_card_mobile_magneto-ui-card-mobile-jobs_18tcb  "><div class="mg_job_card_mobile_magneto-ui-card-mobile-jobs--row1_18tcb"><div class="mg_job_card_mobile_magneto-ui-card-mobile-jobs--brand_18tcb"><img class="mg_job_card_mobile_magneto-ui-card-mobile-jobs--brand_img_18tcb" alt="cadena" src="https://media.magneto365.com/image_assets/files/23460/original-57ccbb0c-a780-4741-bb7a-b0c223ad0112-.png?Expires=1715299199&amp;Key-Pair-Id=KYGE9B84R3EDO&amp;Signature=u5OgOqGajdaF3xW5JzrufgguR8fU6Tm~ETMpVqiHku0j6fXdhVpN8nciiMJybE5Wxg3FUuvw7ZJXqS0cHk7kBeHCWbOwIC0bYVY25oQLu5zX9qiY-O3VQqXNgwcT93tOPMkkHe9Hny9997d6NefHpN5YC-l2piHMNJ9Gx9UAkWw1h8iSicaRndGIjRF8ORDSPb2KHmSPkW30lpliJOfMK8hZarnDe6D5lGgdNt0hlGD8dlJHfhBvXCKno~twAQsrrWYhebiYhvcC-UYaIbvcNRdqnTOfCKfXS1TdNcWLY~XMshxAimcuVyVwyn9dDI8gu2FUpxr7wUvzJ5YKVoyLEg__" loading="lazy" width="50px" height="50px"></div></div><div class="mg_job_card_mobile_magneto-ui-card-mobile-jobs--data_18tcb"><div class="mg_job_card_mobile_magneto-ui-card-mobile-jobs--row2_18tcb"><div><a href="https://www.magneto365.com/co/empleos/analista-de-costos-medellin-b20fd576-7e3f-4ac6-8b04-3e5b22313b6f" title="Analista De Costos" rel="noreferrer"><h2 class="mg_job_card_mobile_magneto-ui-card-mobile-jobs--row2_position_18tcb ">Analista De Costos</h2></a></div><div class="mg_job_card_mobile_magneto-ui-card-mobile-jobs--row2_info_18tcb"><h3>Cadena,</h3><p>Hace  6 horas,</p><p>Caldas - Envigado - Itagui - La Estrella - Medellín (+1)  </p><p>Salario a convenir, </p><p>2 años de experiencia,  </p><p>Técnico, Tecnólogo, Profesional.</p></div></div></div></article><article class="mg_job_card_mobile_magneto-ui-card-mobile-jobs_18tcb  "><div class="mg_job_card_mobile_magneto-ui-card-mobile-jobs--row1_18tcb"><div class="mg_job_card_mobile_magneto-ui-card-mobile-jobs--brand_18tcb"><img class="mg_job_card_mobile_magneto-ui-card-mobile-jobs--brand_img_18tcb" alt="jeronimo-martins" src="https://media.magneto365.com/image_assets/files/17689/original-376bc294-0b76-483e-b2d8-9df008f6593b-.png?Expires=1715299199&amp;Key-Pair-Id=KYGE9B84R3EDO&amp;Signature=SuFUKstOX6Sneq4q~0lirxm4wDUPCTtFtjjpC9pYTzLFbsmAsSQ60log-S-rF8An8zFl1BtQIbB0hnv~Ru4IPPQDg1BhVZyr3WWuB8ac10iBGylFgw5u~Znfwa8jtu81hW0lLSd3LrDED6jMLSmJwXetETD6TPB2PSpTPXWSMh2qXMhDrYUcESXDe-sCoeulpn771cuYUYOsGjyqVtqRjtrkk5JUlZGjO9q0ogYrTfsGyNfI0AcZtYGorxaoa0S2mBdpC2VOBQi1SZVOCedMvaXkefvZIomS3tnKNhhOVMxOWCqjiwxHUtwvf8q54qlOb7gHeADNWOsIAxvmhHAw9Q__" loading="lazy" width="50px" height="50px"></div></div><div class="mg_job_card_mobile_magneto-ui-card-mobile-jobs--data_18tcb"><div class="mg_job_card_mobile_magneto-ui-card-mobile-jobs--row2_18tcb"><div><a href="https://www.magneto365.com/co/empleos/auxiliar-punto-de-venta-caucasia-antioquia-b2dc11f3-ee6d-4d0e-be84-c8f09532eb66" title="Auxiliar Punto De Venta - Caucasia - Antioquia" rel="noreferrer"><h2 class="mg_job_card_mobile_magneto-ui-card-mobile-jobs--row2_position_18tcb ">Auxiliar Punto De Venta - Caucasia - Antioquia</h2></a></div><div class="mg_job_card_mobile_magneto-ui-card-mobile-jobs--row2_info_18tcb"><h3>Ara,</h3><p>Hace  6 horas,</p><p>Caucasia  </p><p>$&nbsp;1.300.000, </p><p>6 meses de experiencia,  </p><p>Bachillerato completo, Técnico, Tecnólogo.</p></div></div></div></article><article class="mg_job_card_mobile_magneto-ui-card-mobile-jobs_18tcb  "><div class="mg_job_card_mobile_magneto-ui-card-mobile-jobs--row1_18tcb"><div class="mg_job_card_mobile_magneto-ui-card-mobile-jobs--brand_18tcb"><img class="mg_job_card_mobile_magneto-ui-card-mobile-jobs--brand_img_18tcb" alt="almacenes-flamingo" src="https://media.magneto365.com/image_assets/files/10400/original-flamingologomagneto-.png?Expires=1715299199&amp;Key-Pair-Id=KYGE9B84R3EDO&amp;Signature=xBlbw6IaO6caX7hCvGXKeDG-7IlmpQixqMiTxPiIIj~gQuf-D~E-2LC327qgHEaI0d048v4Dh54pBUbwP0wsA11C2f-C~cagIh78bTsWlqyqH2HhojgCG0FwB1tEZNtfqZ-SczTl1vjgttmIWn-KnFoGmnupyAQ6QZiDoMfnHEgmgBl17Hhred5aL2swgMGrwW8vyK3pjqyi24mCc54yfqHvBdqp7p4MseDXl5wSPgIge9XXjXl6z1LtpNBCnXFPqyMxCHnNgA6kX-vC9uwNnuP~-tiJdxjMdGcN9PECOgjXXngtOZCl9rMsSrU997ZHZeF~nvipD28q45lpYd-GAw__" loading="lazy" width="50px" height="50px"></div></div><div class="mg_job_card_mobile_magneto-ui-card-mobile-jobs--data_18tcb"><div class="mg_job_card_mobile_magneto-ui-card-mobile-jobs--row2_18tcb"><div><a href="https://www.magneto365.com/co/empleos/aprendiz-t-cnico-en-sistemas-d3d156a1-479a-43d8-ba9c-dda15f1db2ef" title="Aprendiz Técnico en Sistemas" rel="noreferrer"><h2 class="mg_job_card_mobile_magneto-ui-card-mobile-jobs--row2_position_18tcb ">Aprendiz Técnico en Sistemas</h2></a></div><div class="mg_job_card_mobile_magneto-ui-card-mobile-jobs--row2_info_18tcb"><h3>Flamingo,</h3><p>Hace  6 horas,</p><p>Medellín  </p><p>$&nbsp;975.000, </p><p> </p><p>Bachillerato completo, Técnico.</p></div></div></div></article><article class="mg_job_card_mobile_magneto-ui-card-mobile-jobs_18tcb  "><div class="mg_job_card_mobile_magneto-ui-card-mobile-jobs--row1_18tcb"><div class="mg_job_card_mobile_magneto-ui-card-mobile-jobs--brand_18tcb"><img class="mg_job_card_mobile_magneto-ui-card-mobile-jobs--brand_img_18tcb" alt="mibanco" src="https://media.magneto365.com/image_assets/files/15527/original-a_logo_mi_banco_jobsite_header-.png?Expires=1715299199&amp;Key-Pair-Id=KYGE9B84R3EDO&amp;Signature=3U4oc1G60u7zP4t233hirTeJ8U1R8MTNmBI8D16u5CB975viZwh1mftsaKAD3hoEzYrpFBgJrcBB0bwdBOzLZYQ1oePzt4zdInHYFpFJP2erLi0A4cTpJ3c54YaneVC5gZTJkZmCtLNjp0sJhsJm4ShrWRlL~Fkio9j8Rsn22tWsrV2Lhx-YB5EStsYMLoOdLoVKlqbAdP~bBzGpHmuicw1n5DMuTUIxkQW-Zl3~WyRsGlKwOpwrkyFTh8b5nwhTIgurn~Fdl6Wi8-bb826dsdsiJq6CMs~B5Txe9idn79aq7vA4wRMJ4I-PMUpQYZCCy7WmQM3AG33hUpgFL1o-Ug__" loading="lazy" width="50px" height="50px"></div></div><div class="mg_job_card_mobile_magneto-ui-card-mobile-jobs--data_18tcb"><div class="mg_job_card_mobile_magneto-ui-card-mobile-jobs--row2_18tcb"><div><a href="https://www.magneto365.com/co/empleos/asesor-comercial-externo-itagu-41e5dcb7-eb82-4552-a432-2824c50b2a36" title="Asesor comercial externo Itaguí" rel="noreferrer"><h2 class="mg_job_card_mobile_magneto-ui-card-mobile-jobs--row2_position_18tcb ">Asesor comercial externo Itaguí</h2></a></div><div class="mg_job_card_mobile_magneto-ui-card-mobile-jobs--row2_info_18tcb"><h3>Mibanco,</h3><p>Hace  6 horas,</p><p>Itagui  </p><p>Salario a convenir, </p><p>1 año de experiencia,  </p><p>Técnico, Tecnólogo, Profesional.</p></div></div></div></article><article class="mg_job_card_mobile_magneto-ui-card-mobile-jobs_18tcb  "><div class="mg_job_card_mobile_magneto-ui-card-mobile-jobs--row1_18tcb"><div class="mg_job_card_mobile_magneto-ui-card-mobile-jobs--brand_18tcb"><img class="mg_job_card_mobile_magneto-ui-card-mobile-jobs--brand_img_18tcb" alt="magneto-pymes" src="https://media.magneto365.com/image_assets/files/47295/original-9b67ec40-3f98-46ff-a73d-ae20b91a73c4-.png?Expires=1715299199&amp;Key-Pair-Id=KYGE9B84R3EDO&amp;Signature=yD9ioNaAZqQzn1WYfIVCFiDL7N6qkacyoAEaSv-UVaYWBwqFS9yKC9m5O06xBrnzY1VXyRnVZRerRkKAcCVB6cZyTfm5p8ZHwDjOy3MtTeBWhBD2S4QbkUfaqTM8RVAkNjcfECCLDtbNSZhH1rZSMuWpm0XPY6GKPfvEwXL1ym65s2jaxZeXlVuyzL5JjacpgOcMV8Gg6aZQlRxqERn6j7NMyiZEsMMOJ0M1R84rRpBlclYovsfxlDoEP~URkSxJiFnv84adbTak9tkB-AMJDipE7MQINxHbuhH3u9DbXf~G6yCWwxIQQsmt3XetRc59Q3vIPxo~qyieEzsC20m~Mg__" loading="lazy" width="50px" height="50px"></div></div><div class="mg_job_card_mobile_magneto-ui-card-mobile-jobs--data_18tcb"><div class="mg_job_card_mobile_magneto-ui-card-mobile-jobs--row2_18tcb"><div><a href="https://www.magneto365.com/co/empleos/auxiliar-de-tesorer-a-2b9e0b9b-a13c-44c9-b333-536ce6781fc3" title="Auxiliar de tesorería" rel="noreferrer"><h2 class="mg_job_card_mobile_magneto-ui-card-mobile-jobs--row2_position_18tcb ">Auxiliar de tesorería</h2></a></div><div class="mg_job_card_mobile_magneto-ui-card-mobile-jobs--row2_info_18tcb"><h3>DISTRIBUIDORA INTERNACIONAL DE DROGAS SAS,</h3><p>Hace  6 horas,</p><p>Otra (Bogotá D.C.)  </p><p>$&nbsp;1.600.000, </p><p>1 año de experiencia,  </p><p>Técnico, Tecnólogo.</p></div></div></div></article><article class="mg_job_card_mobile_magneto-ui-card-mobile-jobs_18tcb  "><div class="mg_job_card_mobile_magneto-ui-card-mobile-jobs--row1_18tcb"><div class="mg_job_card_mobile_magneto-ui-card-mobile-jobs--brand_18tcb"><img class="mg_job_card_mobile_magneto-ui-card-mobile-jobs--brand_img_18tcb" alt="magneto-pymes" src="https://media.magneto365.com/image_assets/files/52736/original-f2deac3a-c5d5-4886-8ae1-aaf89ed16e39-.png?Expires=1715299199&amp;Key-Pair-Id=KYGE9B84R3EDO&amp;Signature=zQihpyBBcr1ZOFf5vO-ca-ok8VpfY4AbDwAFvvuBd6Dxq5ihZEge19hIqLLtTod8-T~HQAjWTkDBFvNrGdAc1Wv8AlxFtcoRiXPiXAdJlGkHVmq1awGyMEr7RoiOyDC1PRwy6laCz7-~xLxWnxqlXU0Y7ba0hTAbNIZEfYKYyURcEeLnoeIsdzdY1RHq6ojknM73IU8~whZRNYB1OfSOBgbT0vZmC-rc74MEVFv3aAl8qWv6uZTmLpaDitpEfGCI8BXUZh0Qounst2jXDYDyPw3XJWjY9qKquc6kpl3z4~Fa~JK0JMiOH~ZdDvV8db6LttHS8cRuCXisxAca8b4qNg__" loading="lazy" width="50px" height="50px"></div></div><div class="mg_job_card_mobile_magneto-ui-card-mobile-jobs--data_18tcb"><div class="mg_job_card_mobile_magneto-ui-card-mobile-jobs--row2_18tcb"><div><a href="https://www.magneto365.com/co/empleos/dise-ador-grafico-textil-4487e9a3-350e-4267-99cc-dd3a8ad0d03c" title="Diseñador Grafico Textil" rel="noreferrer"><h2 class="mg_job_card_mobile_magneto-ui-card-mobile-jobs--row2_position_18tcb ">Diseñador Grafico Textil</h2></a></div><div class="mg_job_card_mobile_magneto-ui-card-mobile-jobs--row2_info_18tcb"><h3>Accesorios Textiles,</h3><p>Hace  6 horas,</p><p>Medellín  </p><p>$&nbsp;2.200.000 a $&nbsp;2.400.000, </p><p>3 años de experiencia,  </p><p>Tecnólogo, Profesional.</p></div></div></div></article></div>
""""