PGDMP                         y            fyp    13.2    13.2 K               0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false                       0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false                       0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false                       1262    16394    fyp    DATABASE     g   CREATE DATABASE fyp WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'English_United States.1252';
    DROP DATABASE fyp;
                postgres    false            ?            1259    16460    courses    TABLE     U  CREATE TABLE public.courses (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    credit double precision NOT NULL,
    instructor_id integer NOT NULL,
    pre_req character varying(255),
    co_req character varying(255),
    is_lab boolean NOT NULL,
    common character varying(120)[],
    priority integer NOT NULL
);
    DROP TABLE public.courses;
       public         heap    postgres    false            ?            1259    16458    courses_id_seq    SEQUENCE     ?   CREATE SEQUENCE public.courses_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 %   DROP SEQUENCE public.courses_id_seq;
       public          postgres    false    211                       0    0    courses_id_seq    SEQUENCE OWNED BY     A   ALTER SEQUENCE public.courses_id_seq OWNED BY public.courses.id;
          public          postgres    false    210            ?            1259    16447    halls    TABLE     ?   CREATE TABLE public.halls (
    id integer NOT NULL,
    specialty_id integer NOT NULL,
    is_lab boolean NOT NULL,
    building character varying(255)
);
    DROP TABLE public.halls;
       public         heap    postgres    false            ?            1259    16445    halls_id_seq    SEQUENCE     ?   CREATE SEQUENCE public.halls_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 #   DROP SEQUENCE public.halls_id_seq;
       public          postgres    false    209                       0    0    halls_id_seq    SEQUENCE OWNED BY     =   ALTER SEQUENCE public.halls_id_seq OWNED BY public.halls.id;
          public          postgres    false    208            ?            1259    16417    instructors    TABLE     ?   CREATE TABLE public.instructors (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    specialty integer NOT NULL
);
    DROP TABLE public.instructors;
       public         heap    postgres    false            ?            1259    16415    instructors_id_seq    SEQUENCE     ?   CREATE SEQUENCE public.instructors_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 )   DROP SEQUENCE public.instructors_id_seq;
       public          postgres    false    205                       0    0    instructors_id_seq    SEQUENCE OWNED BY     I   ALTER SEQUENCE public.instructors_id_seq OWNED BY public.instructors.id;
          public          postgres    false    204            ?            1259    16397    specialtyInCollege    TABLE     p   CREATE TABLE public."specialtyInCollege" (
    id integer NOT NULL,
    name character varying(255) NOT NULL
);
 (   DROP TABLE public."specialtyInCollege";
       public         heap    postgres    false            ?            1259    16395    specialtyInCollege_id_seq    SEQUENCE     ?   CREATE SEQUENCE public."specialtyInCollege_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 2   DROP SEQUENCE public."specialtyInCollege_id_seq";
       public          postgres    false    201                       0    0    specialtyInCollege_id_seq    SEQUENCE OWNED BY     [   ALTER SEQUENCE public."specialtyInCollege_id_seq" OWNED BY public."specialtyInCollege".id;
          public          postgres    false    200            ?            1259    16432    studentPlan    TABLE     ?   CREATE TABLE public."studentPlan" (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    specialty integer NOT NULL
);
 !   DROP TABLE public."studentPlan";
       public         heap    postgres    false            ?            1259    16478    studentPlanCourses    TABLE     ?   CREATE TABLE public."studentPlanCourses" (
    id integer NOT NULL,
    student_plan_id integer NOT NULL,
    level integer NOT NULL,
    course_id integer NOT NULL
);
 (   DROP TABLE public."studentPlanCourses";
       public         heap    postgres    false            ?            1259    16476    studentPlanCourses_id_seq    SEQUENCE     ?   CREATE SEQUENCE public."studentPlanCourses_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 2   DROP SEQUENCE public."studentPlanCourses_id_seq";
       public          postgres    false    213                       0    0    studentPlanCourses_id_seq    SEQUENCE OWNED BY     [   ALTER SEQUENCE public."studentPlanCourses_id_seq" OWNED BY public."studentPlanCourses".id;
          public          postgres    false    212            ?            1259    16430    studentPlan_id_seq    SEQUENCE     ?   CREATE SEQUENCE public."studentPlan_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 +   DROP SEQUENCE public."studentPlan_id_seq";
       public          postgres    false    207                       0    0    studentPlan_id_seq    SEQUENCE OWNED BY     M   ALTER SEQUENCE public."studentPlan_id_seq" OWNED BY public."studentPlan".id;
          public          postgres    false    206            ?            1259    16735 	   timetable    TABLE     H  CREATE TABLE public.timetable (
    id integer NOT NULL,
    specialty_id integer NOT NULL,
    course_id integer NOT NULL,
    hall_id integer NOT NULL,
    instructor_id integer NOT NULL,
    start_time double precision NOT NULL,
    end_time double precision NOT NULL,
    day integer NOT NULL,
    level integer NOT NULL
);
    DROP TABLE public.timetable;
       public         heap    postgres    false            ?            1259    16733    timetable_id_seq    SEQUENCE     ?   CREATE SEQUENCE public.timetable_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 '   DROP SEQUENCE public.timetable_id_seq;
       public          postgres    false    215                       0    0    timetable_id_seq    SEQUENCE OWNED BY     E   ALTER SEQUENCE public.timetable_id_seq OWNED BY public.timetable.id;
          public          postgres    false    214            ?            1259    16407    worktime    TABLE     
  CREATE TABLE public.worktime (
    id integer NOT NULL,
    day integer NOT NULL,
    start_time time without time zone NOT NULL,
    end_time time without time zone NOT NULL,
    break_time_start time without time zone,
    break_time_end time without time zone
);
    DROP TABLE public.worktime;
       public         heap    postgres    false            ?            1259    16405    workTime_id_seq    SEQUENCE     ?   CREATE SEQUENCE public."workTime_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 (   DROP SEQUENCE public."workTime_id_seq";
       public          postgres    false    203                       0    0    workTime_id_seq    SEQUENCE OWNED BY     E   ALTER SEQUENCE public."workTime_id_seq" OWNED BY public.worktime.id;
          public          postgres    false    202            R           2604    16463 
   courses id    DEFAULT     h   ALTER TABLE ONLY public.courses ALTER COLUMN id SET DEFAULT nextval('public.courses_id_seq'::regclass);
 9   ALTER TABLE public.courses ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    211    210    211            Q           2604    16450    halls id    DEFAULT     d   ALTER TABLE ONLY public.halls ALTER COLUMN id SET DEFAULT nextval('public.halls_id_seq'::regclass);
 7   ALTER TABLE public.halls ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    209    208    209            O           2604    16420    instructors id    DEFAULT     p   ALTER TABLE ONLY public.instructors ALTER COLUMN id SET DEFAULT nextval('public.instructors_id_seq'::regclass);
 =   ALTER TABLE public.instructors ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    204    205    205            M           2604    16400    specialtyInCollege id    DEFAULT     ?   ALTER TABLE ONLY public."specialtyInCollege" ALTER COLUMN id SET DEFAULT nextval('public."specialtyInCollege_id_seq"'::regclass);
 F   ALTER TABLE public."specialtyInCollege" ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    200    201    201            P           2604    16435    studentPlan id    DEFAULT     t   ALTER TABLE ONLY public."studentPlan" ALTER COLUMN id SET DEFAULT nextval('public."studentPlan_id_seq"'::regclass);
 ?   ALTER TABLE public."studentPlan" ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    207    206    207            S           2604    16481    studentPlanCourses id    DEFAULT     ?   ALTER TABLE ONLY public."studentPlanCourses" ALTER COLUMN id SET DEFAULT nextval('public."studentPlanCourses_id_seq"'::regclass);
 F   ALTER TABLE public."studentPlanCourses" ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    212    213    213            T           2604    16738    timetable id    DEFAULT     l   ALTER TABLE ONLY public.timetable ALTER COLUMN id SET DEFAULT nextval('public.timetable_id_seq'::regclass);
 ;   ALTER TABLE public.timetable ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    214    215    215            N           2604    16410    worktime id    DEFAULT     l   ALTER TABLE ONLY public.worktime ALTER COLUMN id SET DEFAULT nextval('public."workTime_id_seq"'::regclass);
 :   ALTER TABLE public.worktime ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    203    202    203                      0    16460    courses 
   TABLE DATA           m   COPY public.courses (id, name, credit, instructor_id, pre_req, co_req, is_lab, common, priority) FROM stdin;
    public          postgres    false    211   ?Y                 0    16447    halls 
   TABLE DATA           C   COPY public.halls (id, specialty_id, is_lab, building) FROM stdin;
    public          postgres    false    209   \\                  0    16417    instructors 
   TABLE DATA           :   COPY public.instructors (id, name, specialty) FROM stdin;
    public          postgres    false    205   ?\       ?          0    16397    specialtyInCollege 
   TABLE DATA           8   COPY public."specialtyInCollege" (id, name) FROM stdin;
    public          postgres    false    201   z]                 0    16432    studentPlan 
   TABLE DATA           <   COPY public."studentPlan" (id, name, specialty) FROM stdin;
    public          postgres    false    207   ?]                 0    16478    studentPlanCourses 
   TABLE DATA           U   COPY public."studentPlanCourses" (id, student_plan_id, level, course_id) FROM stdin;
    public          postgres    false    213   ?]       
          0    16735 	   timetable 
   TABLE DATA           z   COPY public.timetable (id, specialty_id, course_id, hall_id, instructor_id, start_time, end_time, day, level) FROM stdin;
    public          postgres    false    215   ?^       ?          0    16407    worktime 
   TABLE DATA           c   COPY public.worktime (id, day, start_time, end_time, break_time_start, break_time_end) FROM stdin;
    public          postgres    false    203   ?`                  0    0    courses_id_seq    SEQUENCE SET     =   SELECT pg_catalog.setval('public.courses_id_seq', 87, true);
          public          postgres    false    210                       0    0    halls_id_seq    SEQUENCE SET     ;   SELECT pg_catalog.setval('public.halls_id_seq', 1, false);
          public          postgres    false    208                       0    0    instructors_id_seq    SEQUENCE SET     A   SELECT pg_catalog.setval('public.instructors_id_seq', 32, true);
          public          postgres    false    204                       0    0    specialtyInCollege_id_seq    SEQUENCE SET     J   SELECT pg_catalog.setval('public."specialtyInCollege_id_seq"', 1, false);
          public          postgres    false    200                       0    0    studentPlanCourses_id_seq    SEQUENCE SET     J   SELECT pg_catalog.setval('public."studentPlanCourses_id_seq"', 47, true);
          public          postgres    false    212                       0    0    studentPlan_id_seq    SEQUENCE SET     B   SELECT pg_catalog.setval('public."studentPlan_id_seq"', 5, true);
          public          postgres    false    206                       0    0    timetable_id_seq    SEQUENCE SET     @   SELECT pg_catalog.setval('public.timetable_id_seq', 459, true);
          public          postgres    false    214                        0    0    workTime_id_seq    SEQUENCE SET     @   SELECT pg_catalog.setval('public."workTime_id_seq"', 10, true);
          public          postgres    false    202            h           2606    16470    courses courses_name_key 
   CONSTRAINT     S   ALTER TABLE ONLY public.courses
    ADD CONSTRAINT courses_name_key UNIQUE (name);
 B   ALTER TABLE ONLY public.courses DROP CONSTRAINT courses_name_key;
       public            postgres    false    211            j           2606    16468    courses courses_pkey 
   CONSTRAINT     R   ALTER TABLE ONLY public.courses
    ADD CONSTRAINT courses_pkey PRIMARY KEY (id);
 >   ALTER TABLE ONLY public.courses DROP CONSTRAINT courses_pkey;
       public            postgres    false    211            f           2606    16452    halls halls_pkey 
   CONSTRAINT     N   ALTER TABLE ONLY public.halls
    ADD CONSTRAINT halls_pkey PRIMARY KEY (id);
 :   ALTER TABLE ONLY public.halls DROP CONSTRAINT halls_pkey;
       public            postgres    false    209            ^           2606    16424     instructors instructors_name_key 
   CONSTRAINT     [   ALTER TABLE ONLY public.instructors
    ADD CONSTRAINT instructors_name_key UNIQUE (name);
 J   ALTER TABLE ONLY public.instructors DROP CONSTRAINT instructors_name_key;
       public            postgres    false    205            `           2606    16422    instructors instructors_pkey 
   CONSTRAINT     Z   ALTER TABLE ONLY public.instructors
    ADD CONSTRAINT instructors_pkey PRIMARY KEY (id);
 F   ALTER TABLE ONLY public.instructors DROP CONSTRAINT instructors_pkey;
       public            postgres    false    205            V           2606    16404 .   specialtyInCollege specialtyInCollege_name_key 
   CONSTRAINT     m   ALTER TABLE ONLY public."specialtyInCollege"
    ADD CONSTRAINT "specialtyInCollege_name_key" UNIQUE (name);
 \   ALTER TABLE ONLY public."specialtyInCollege" DROP CONSTRAINT "specialtyInCollege_name_key";
       public            postgres    false    201            X           2606    16402 *   specialtyInCollege specialtyInCollege_pkey 
   CONSTRAINT     l   ALTER TABLE ONLY public."specialtyInCollege"
    ADD CONSTRAINT "specialtyInCollege_pkey" PRIMARY KEY (id);
 X   ALTER TABLE ONLY public."specialtyInCollege" DROP CONSTRAINT "specialtyInCollege_pkey";
       public            postgres    false    201            l           2606    16483 *   studentPlanCourses studentPlanCourses_pkey 
   CONSTRAINT     l   ALTER TABLE ONLY public."studentPlanCourses"
    ADD CONSTRAINT "studentPlanCourses_pkey" PRIMARY KEY (id);
 X   ALTER TABLE ONLY public."studentPlanCourses" DROP CONSTRAINT "studentPlanCourses_pkey";
       public            postgres    false    213            b           2606    16439     studentPlan studentPlan_name_key 
   CONSTRAINT     _   ALTER TABLE ONLY public."studentPlan"
    ADD CONSTRAINT "studentPlan_name_key" UNIQUE (name);
 N   ALTER TABLE ONLY public."studentPlan" DROP CONSTRAINT "studentPlan_name_key";
       public            postgres    false    207            d           2606    16437    studentPlan studentPlan_pkey 
   CONSTRAINT     ^   ALTER TABLE ONLY public."studentPlan"
    ADD CONSTRAINT "studentPlan_pkey" PRIMARY KEY (id);
 J   ALTER TABLE ONLY public."studentPlan" DROP CONSTRAINT "studentPlan_pkey";
       public            postgres    false    207            n           2606    16740    timetable timetable_pkey 
   CONSTRAINT     V   ALTER TABLE ONLY public.timetable
    ADD CONSTRAINT timetable_pkey PRIMARY KEY (id);
 B   ALTER TABLE ONLY public.timetable DROP CONSTRAINT timetable_pkey;
       public            postgres    false    215            Z           2606    16414    worktime worktime_day_key 
   CONSTRAINT     S   ALTER TABLE ONLY public.worktime
    ADD CONSTRAINT worktime_day_key UNIQUE (day);
 C   ALTER TABLE ONLY public.worktime DROP CONSTRAINT worktime_day_key;
       public            postgres    false    203            \           2606    16412    worktime worktime_pkey 
   CONSTRAINT     T   ALTER TABLE ONLY public.worktime
    ADD CONSTRAINT worktime_pkey PRIMARY KEY (id);
 @   ALTER TABLE ONLY public.worktime DROP CONSTRAINT worktime_pkey;
       public            postgres    false    203            r           2606    16471 "   courses courses_instructor_id_fkey    FK CONSTRAINT     ?   ALTER TABLE ONLY public.courses
    ADD CONSTRAINT courses_instructor_id_fkey FOREIGN KEY (instructor_id) REFERENCES public.instructors(id);
 L   ALTER TABLE ONLY public.courses DROP CONSTRAINT courses_instructor_id_fkey;
       public          postgres    false    2912    211    205            q           2606    16453    halls halls_specialty_id_fkey    FK CONSTRAINT     ?   ALTER TABLE ONLY public.halls
    ADD CONSTRAINT halls_specialty_id_fkey FOREIGN KEY (specialty_id) REFERENCES public."specialtyInCollege"(id);
 G   ALTER TABLE ONLY public.halls DROP CONSTRAINT halls_specialty_id_fkey;
       public          postgres    false    201    209    2904            o           2606    16425 &   instructors instructors_specialty_fkey    FK CONSTRAINT     ?   ALTER TABLE ONLY public.instructors
    ADD CONSTRAINT instructors_specialty_fkey FOREIGN KEY (specialty) REFERENCES public."specialtyInCollege"(id);
 P   ALTER TABLE ONLY public.instructors DROP CONSTRAINT instructors_specialty_fkey;
       public          postgres    false    201    205    2904            t           2606    16489 4   studentPlanCourses studentPlanCourses_course_id_fkey    FK CONSTRAINT     ?   ALTER TABLE ONLY public."studentPlanCourses"
    ADD CONSTRAINT "studentPlanCourses_course_id_fkey" FOREIGN KEY (course_id) REFERENCES public.courses(id);
 b   ALTER TABLE ONLY public."studentPlanCourses" DROP CONSTRAINT "studentPlanCourses_course_id_fkey";
       public          postgres    false    211    213    2922            s           2606    16484 :   studentPlanCourses studentPlanCourses_student_plan_id_fkey    FK CONSTRAINT     ?   ALTER TABLE ONLY public."studentPlanCourses"
    ADD CONSTRAINT "studentPlanCourses_student_plan_id_fkey" FOREIGN KEY (student_plan_id) REFERENCES public."studentPlan"(id);
 h   ALTER TABLE ONLY public."studentPlanCourses" DROP CONSTRAINT "studentPlanCourses_student_plan_id_fkey";
       public          postgres    false    213    207    2916            p           2606    16440 &   studentPlan studentPlan_specialty_fkey    FK CONSTRAINT     ?   ALTER TABLE ONLY public."studentPlan"
    ADD CONSTRAINT "studentPlan_specialty_fkey" FOREIGN KEY (specialty) REFERENCES public."specialtyInCollege"(id);
 T   ALTER TABLE ONLY public."studentPlan" DROP CONSTRAINT "studentPlan_specialty_fkey";
       public          postgres    false    2904    201    207            v           2606    16746 "   timetable timetable_course_id_fkey    FK CONSTRAINT     ?   ALTER TABLE ONLY public.timetable
    ADD CONSTRAINT timetable_course_id_fkey FOREIGN KEY (course_id) REFERENCES public.courses(id);
 L   ALTER TABLE ONLY public.timetable DROP CONSTRAINT timetable_course_id_fkey;
       public          postgres    false    2922    211    215            w           2606    16751     timetable timetable_hall_id_fkey    FK CONSTRAINT        ALTER TABLE ONLY public.timetable
    ADD CONSTRAINT timetable_hall_id_fkey FOREIGN KEY (hall_id) REFERENCES public.halls(id);
 J   ALTER TABLE ONLY public.timetable DROP CONSTRAINT timetable_hall_id_fkey;
       public          postgres    false    209    215    2918            x           2606    16756 &   timetable timetable_instructor_id_fkey    FK CONSTRAINT     ?   ALTER TABLE ONLY public.timetable
    ADD CONSTRAINT timetable_instructor_id_fkey FOREIGN KEY (instructor_id) REFERENCES public.instructors(id);
 P   ALTER TABLE ONLY public.timetable DROP CONSTRAINT timetable_instructor_id_fkey;
       public          postgres    false    205    2912    215            u           2606    16741 %   timetable timetable_specialty_id_fkey    FK CONSTRAINT     ?   ALTER TABLE ONLY public.timetable
    ADD CONSTRAINT timetable_specialty_id_fkey FOREIGN KEY (specialty_id) REFERENCES public."specialtyInCollege"(id);
 O   ALTER TABLE ONLY public.timetable DROP CONSTRAINT timetable_specialty_id_fkey;
       public          postgres    false    215    201    2904               ?  x????n?0Ek?[?@? E????pd?	?:e*wF?=??????c?s9"?<0?~???H	??o??;}̗???????o???F?
|?`U?*L{ ʊ?sQQ???D??t=??	?.???!?f???"???(l??vAQ??z?N?D!???)?8??0zY???J??l1l?Q4?E?ET?ѯ?A?yK{??
???B??? S?*?a ???M??f???K)i>???1?RN'????Aw???@Y??Ϝ$h?ӘzQ??@???"X6 ?P}?ϼ;??y??"??'E?'Q?@i?? ????P??H,??ߍ?~j8}3/0*E?????-?] ?u%?ޙ.??||?????*?	E6ǔuR?KR?V?0?(?֫????u"???m-TN^??>??????Z'?+?D
P???,;k?߳wU٥?T?rr??(V?Z3y? ??y??ɗ??B}-b9?$??G??iû?4??????8$?@??Q^????O?M????Oܦ???? b%?'??d%?꣋->
??}??ͺG
w????]іj?X:???ƍ???=ug??x???[?%B????U????j????????B???(???
M?NG?j???6??6?tL???5??N?ZjM#???z?蘾}??
p?         [   x?E?+?0@??!?? P?hN??)?k܊zh=Y? D ??:
P????cc???TgpFc????Y(??/?:?@*Cjj??P?_?A):          ?   x?%ϻ?0???cP???0?bbeq?!m??????vl_Y??u??t?ZXhc??a#??`sE?3??9???J?.$53b&??????Pc!??0???-3StXJ??O???D?n???m???/I?	?@k???????4x~An???3ЛZ?:)?~?7:?      ?      x?3?t?2???2?t?w?????? (??            x?3?t?4?????? ??         ?   x?%???E1?s\?*??^~?u,??G \??`?|?Τ#*???????x?Hp?.Ȗ@k??????ҙ?h???r??ޗm??H?	????
?f)?怾???B	??Cj)!?ڃ??b?&bT?d?7tG?^????%?92?????ߎ????e	??x??? ?#+4S      
   *  x?eT?q? ?N??l٥??QI&?^??˫?%A쾎r?>o<?iw????(e?h?*??u?vh!?k????*(?(???\?@[?>?Z[?v?qu{?G-?????TZ?_@'&??~q?[?????:?zl<?SH5̈???C????4?? (??hG3?HH???&j?f{?o@?????*1???Kk??9?pEb??7?L?lw6?i???R?M?????7?=JC?X?m?ô"??=?]??P?-?Ǵd??/??x铑h??/	 *U??`???h\:?T0?Jr_?j(??q??]????%q????=???-?]?<?=O??)-??!?B??\???haW??VF?6Ou_??1?Ӡ?\???W>FK?3???'??|?;?d$???Յ???g??ӎ?R|?<??B?nk?k????+??????d?z???H?OBΉܾ	9w?&?D|??Rm{?"?κ8??l??NS]???)??q??/?h8ݎ?]z?ãЋ??䵜e,?R??ӣ??Z????;?+!8i?-!['???C??n?,gy齳?Lǖ???<??p???      ?   5   x???4?4??20 "NCs(#???,9Mp?p???4?4­???\? ??     