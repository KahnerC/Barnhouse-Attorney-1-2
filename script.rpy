# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define har = Character("Jesse", image="har")#Jesse Barnhouse
define udge = Character("Marilyn", image="udge")#Marilyn Mason
define mik = Character("Sharon", image="mik")
define kyo = Character("Lachlan", image="kyo")#Lachlan Pyre
define koi = Character("Hugh", image="koi")
define tsu = Character("Ann", image="tsu")#Annabel Whitni
define yuk = Character("Ellen")#Ellen Detente
define des = Character(" ")#Descriptions


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    python:
        h_1 = "Jesse"
        h_2 = "Barnhouse"
        h_3 = "Jess"
        u_1 = "Marilyn"
        u_2 = "Mason"
        m_1 = "Sharon"
        m_2 = "Zephyr"
        m_3 = "Shaz"
        k_1 = "Hugh"
        k_2 = "Lester-Dobsmouth"
        k_3 = "Hugh"
        ky_1 = "Lachlan"
        ky_2 = "Pyre"
        ky_3 = "Lachy"
        t_1 = "Ann"
        t_2 = "Whitni"
        t_3 = "Ann"
        y_1 = "Ellen"
        y_2 = "Detente"
        y_3 = "Ellen"
        sos_1 = "Groovy Gang"

    jump case_1_2_2

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
    
label case_1_2_2:
    
    play music "Alexander Ehlers - Spacetime.mp3"
    des "Some day, some month, afternoon maybe. 15:22 o'clock pm\nSchool Court, First Courtroom"
    udge "Trial is about to begin. Are both sides ready?"
    har confident "The defense is ready."
    koi "The prosecution is ready, your honour."
    udge blink "Today's trial will be an odd one."
    udge -blink "The victim, Ms [m_1] [m_2] does not recall the exact events,"
    udge "and we do not know what crime, if any has been committed against her."
    udge "Still, we will proceed without a charge, to determine if police intervention is warranted."
    kyo "What's happening now?"
    har think "It's just like [u_1] said, we're going to piece some truth a few incomplete tales."
    har "If we're lucky, we'll jog [m_1]'s memory enough by the end to get a clear picture."
    har -think "You'll be nominally playing the role of defendant, to keep proper court procedure."
    kyo suspicious "I see."
    udge "Mister [k_2], please give your opening statement."
    koi "Victim [m_1] [m_2] was discovered unconscious in the literature club room a few hours ago."
    koi smug "She was discovered by [h_1] [h_2]."
    koi -smug "There were a number of photographs scattered about the scene."
    udge surprise ".."
    udge -surprise "I see. There are some very interesting outfits in these."
    koi deskslam "The prosecution would like to submit these as evidence."

    show cr4
    "'Loose Photographs' added to the court record."
    koi "We would also like to submit some of the costumes found in the literature club."
    show cr1
    "'Hot Dog Costume' added to the court record."
    show cr3
    "'Guy Fawkes Mask and Cloak' added to the court record."
    show cr2
    "'Rabbit Costume' added to the court record."
    udge "That's quite a few."
    koi smug "It's all we could match to the photographs."
    udge "Very well. Let's hear from the victim."
    koi point "Of course. Victim, as a formality, your name and occupation?"
    mik "[m_1] [m_2], ah, student."
    har deskslam ".."
    mik sad "Member of the [sos_1]."
    koi "Now, Ms [m_2], please tell us what you remember about the incident."
    show side mik
    "{color=#0000ffff}Testimony\n[m_1]'s Recollection of Events"

    #TESTIMONY
    call cross_examine("MIKURU", 1) from _call_cross_examine
    
    har think "(Short and sweet. Like [m_1] herself.)"
    har "(This could definitely be sketchy enough to be a police matter.)"
    udge "Defense, please begin your cross-examination."
    har confident "Let's have at it."

    #CROSS EXAMINATION
    call cross_examine("MIKURU") from _call_cross_examine_1

    scene black
    des "Same day, same month. 16:14 pm\nSchool Court, First Courtroom"
    show side udge
    udge "Welcome back, gang."
    udge "As luck would have it, we managed to pin down our witness."
    tsu "Howdy howdy."
    udge "We are all aware of the circumstances but, for Ms [t_2]'s benefit, the facts are:"
    udge blink "[m_1] [m_2] was found unconscious in the literary club room after school today."
    udge -blink "Ms [m_2]'s testimony tells that she and Ms [t_2] were trying on outfits during lunch."
    udge "Photographs of Ms [m_2] in these costumes were found at the scene."
    udge "Police involvement may be deemed necessary, depending on what is determined today. There is no specific charge at this time."
    udge "Ms [m_2], do you understand?"
    tsu "I understand fine."
    udge "Prosecution, your witness."
    koi point "As a formality, your name and occupation."
    tsu "[t_1] [t_2], student."
    koi "[t_1], Ms [m_2]'s memory of today's events is somewhat hazy."
    koi -point "Would you recite to the court your understanding of the events."
    tsu guarded "Yes, I suppose I will."

    show side tsu
    "{color=#0000ffff}Testimony\n[t_1]'s Recollection of Events"

    #TESTIMONY
    
    call cross_examine("TSURUYA", 1) from _call_cross_examine_2

    tsu "Well, that's how it is."
    koi "I see."
    udge angry "This is starting to sound like a police matter."
    udge -angry "It may be best to stop the trial here."
    har confident "The defense will continue with it's cross-examination."
    koi "Agreed. The prosecution also feels that further information is needed."
    udge "We will proceed with the trial."
    tsu guarded".."

    #CROSS EXAMINATION
    call cross_examine("TSURUYA") from _call_cross_examine_3

    udge "What do you mean by that?"
    udge "We could have her testify again if you can give a good reason."
    har confident "([t_3] can testify all day and get us nowhere.)"
    har think "(Our mystery pervert doesn't have much of a presence outside of that fiddlestick of a testimony.)"
    har deskslam "Your honour, I don't believe [t_1]'s claim of a suspicious person."
    udge angry "Believe what you want, [h_1], but this is a courtroom."
    har paper"[m_1]'s testimony made no mention of a suspicious person, or any commotion outside."
    har -paper"Klutz or not, she wouldn't have missed that."
    udge surprise "Do you mean to say that you have another culprit in mind?"

    har confident "Sure do."
    har think "([t_3] is lying, and there's only one person she would have to cover for.)"
    har "(I'd better take another look at the evidence.)"

    har confident "I've solved it."
    udge "Nicely done, [h_2]."
    udge blink "Great.."
    udge -blink "But what do you mean?"
    udge surprise "Who did it?"

    #presenting a culprit 14689
    
    
    
    label accuse_tsu:
    menu:
        "The mystery man did it.":
            har confident "[t_1]'s mystery man did it."
            udge angry "That isn't an answer."
            jump accuse_tsu
        "[ky_1] did it.":
            har confident "[ky_1] did it all. Can't trust him."
            udge "He does look shifty."
            koi smug "As the prosecution, I am inclined to agree."
            udge "I'm about ready to call a verdict."
            kyo confused "But.."
            har offguard "As your attorney, you have to trust me with these things."
            jump accuse_tsu
        "[t_1] did it.":
            pass
        "[y_1] did it.":
            har point "It was the [sos_1]'s very own [y_1] [y_2] that did it."
            udge "But she has nothing to do with the trial."
            har confident "Exactly. The perfect alibi."
            udge angry "Come up with a real suspect."  
            jump accuse_tsu
    
    #"PRESENTING TSURUYA AS CULPRIT"

    har point "[t_1] did it."
    tsu offguard "What??"
    udge angry "Defense, please provide some evidence to support this claim."
    har think "(I'd better have this straight.)"

    label accuse_tsu_prove:
    menu:
        "The Guy Fawkes mask and cloak proves it.":
            har confident "The Guy Fawkes mask and cloak proves it."
            tsu ".."
            koi ".."
            udge angry ".."
            har damage "(I had better rethink that.)"
            jump accuse_tsu_prove
        "The rabbit costume proves it.":
            har confident "The rabbit costume proves it."
            tsu ".."
            koi ".."
            udge angry ".."
            har damage "(I had better rethink that.)"
            jump accuse_tsu_prove
        "The hot dog costume proves it.":
            har confident "The hot dog costume proves it."
            tsu ".."
            koi ".."
            udge angry ".."
            har damage "(I had better rethink that.)"
            jump accuse_tsu_prove
        "This photo proves it.":
            pass

    har paper "Take a look at this here picture."

    har "At a glance, you might think the green is just some overhanging foliage."
    har deskslam "On closer inspection, that's..."
    label accuse_hair:
    menu:
        "It's a plant.":
            har "On closer inspection, that is indeed overhanging foliage."
            har "Looks nice."
            har think "You should get some plants for this courtroom."
            har offguard "Spruce it up."
            har "Some ferns. A vase, maybe."
            udge angry "[h_1], I won't cut fresh flowers for you."
            har damage "(Small talk won't get me anywhere fast.)"
            jump accuse_hair
        "It's hair.":
            har confident "It's hair. [t_1]'s hair."
        "It's a smudge.":
            har deskslam "It's a smudge."
            koi deskslam "It isn't a smudge."
            udge angry "Objection sustained."
            jump accuse_hair
    tsu offguard "What??"
    udge surprise ".."
    udge "It definitely isn't a natural green, but.."
    udge "What would [t_1]'s hair be doing in a place like this?"
    udge -surprise "Explain yourself."

    #accusation mode 15117
    #"ACCUSATION ZOOM AND BACKGROUND"

    play music "Alexander Ehlers - Doomed.mp3"

    har accuse "It's simple."
    har accuse "This places [t_1] at the scene of the crime."
    har accuse "Giving the the placement, the angle, the hair and [t_1]'s shaky recollection, there can only be one explanation."
    udge "Explain yourself."
    har accuse "[t_1] was the one who took the picture."
    #END ACCUSATION
    #"END ACCUSATION"

    har confident "It's dead simple. [m_1] and [t_1] were chatting about in the clubroom, when [t_1] decided to take a sneaky picture."
    har point "[m_1] spotted her and tried to confiscate it. Having failed that, the picture was no doubt used to blackmail her into silence."

    tsu "Well."
    #play music "Alexander Ehlers - Spacetime.mp3"
    tsu offguard "..."
    tsu "It's all true."

    tsu guarded "You’d find it easier to be bad than good if you had green hair. People who haven’t green hair don’t know what trouble is. Oh, [h_1], you little know how utterly wretched I am."
    mik s "But why?"
    tsu guarded "Everyone says [m_1] is so beautiful, that her voice is like music and her eyes like pansies when the dew is on them. She's like a tall stately queen and her hair is like rippling gold."
    tsu "When she asked about how lovely it must be to dress as grown-ups, the iron had entered into my soul."
    tsu -guarded "I just had to take a picture and show it around."
    har deskslam "Indeed. I will have to see the picture."
    har -deskslam"It certainly looks like the facts of the case have been laid bare."
    udge "Agreed. Ms [t_2] is certainly guilty of taking indecent photographs of Ms [m_2] without permission,"
    udge blink "of blackmail, perjury, and of wasting court time and resources."
    udge -blink "However, as this is not a real court, I leave you to resolve the consequences among yourselves."
    har think "As long as I get to see the rest of those pictures."
    tsu surprise "Oh, indeed, [h_1], I do want to show them."
    mik s burst ".."
    
    return

    label cross_examine(tes_name="NONE",tes_only=0):
        
        python:
            poses = {
                "m_blink":"side mik blink",
                "m_burst":"side mik burst",
                "m_sad":"side mik sad",
                "m_thinking":"side mik think",
                "m":"side mik",
                "t_guarded":"side tsu guarded",
                "t_offguard":"side tsu offguard",
                "t":"side tsu"
            }
            tes_index = 0
            tes_index_prev = 0
            tes_end_loop = 0
            tes_return = 0
            if tes_name=="MIKURU":
                tes_speaker = m_1
                tes_bool = [1,0,0,0,0,0,1]
                tes_values = [
                    "I went to the club room during lunch.",
                    "I got a text saying my dry-cleaning was ready, so I picked it up on the way to school.",
                    "But it was all so odd-shaped and bulky and awkward to carry.",
                    "It was difficult to carry because of the sheer volume.",
                    "We barely managed to get it in.",
                    "And we started talking about the outfits.",
                    "Then, next thing I remember, Ms [h_2] was shaking me.".replace("[h_2]",h_2)
                    ]
                tes_poses = ["m","m_blink","m","m_thinking","m_sad","m","m_blink"]
            elif tes_name == "TSURUYA":
                tes_bool = [1,1,1,1,0,0,0,0,0,0]
                tes_values = [
                            "I went to the literature club room with [m_1] at lunch.".replace("[m_1]",m_1),
                            "We were showing off costumes to each other.",
                            "There was a strange presence at the door.",
                            "I investigated, and was attacked. I passed out soon after.",
                            "I investigated, and saw someone taking photos outside the door.",
                            "I was attacked.",
                            "He was in his late forties, balding, heavily tattooed and wearing an eyepatch.",
                            "I had to go to the bathroom for a little while.",
                            "And when I got back, I saw someone taking photos outside the door.",
                            "I woke up in the infirmary after."                            
                            ]
                tes_poses = ["t","t","t_guarded","t","t","t","t_offguard","t_guarded","t_offguard","t"]
            else:
                tes_bool = [1,1,0,1,0]
                tes_values = ["Y","N","M","IDK","CYRTC"]
            tes_size = len(tes_bool)
            tes_line = tes_values[tes_index]
            #for i in range(tes_size):
            #    tes_poses[i] = poses[tes_poses[i]]
            #tes_image = poses[tes_poses[tes_index]] + ".png"
            while tes_bool[tes_index] < 1:
                tes_index = (tes_index + 1) % tes_size
        
        label tes_start:
        
        #show str(poses[tes_poses[tes_index]] + ".png")
        #image witness = poses[tes_poses[tes_index]] + ".png"
        #show witness
        $ tes_image = poses[tes_poses[tes_index]] + ".png"
        image witness = "[tes_image]"
        show witness
        if tes_return > 0:
            $ tes_return = 0
            return
        if tes_only > 0:
            tes_speaker "{color=#00ff00}[tes_line]"
            python:
                tes_index = (tes_index + 1) % tes_size
                if tes_index == 0:
                    tes_return = 1
                while tes_bool[tes_index] < 1:
                    tes_index = (tes_index + 1) % tes_size
                    if tes_index == 0:
                        tes_return = 1
            $ tes_line = tes_values[tes_index]
        else:
            menu:
                tes_speaker "{color=#00ff00}[tes_line]"
                "<":
                    python:
                        tes_index = (tes_index - 1) % tes_size
                        while tes_bool[tes_index] < 1:
                            tes_index = (tes_index - 1) % tes_size
                ">":
                    python:
                        tes_index_prev = tes_index
                        tes_index = (tes_index + 1) % tes_size
                        while tes_bool[tes_index] < 1:
                            tes_index = (tes_index + 1) % tes_size
                        if tes_index_prev > tes_index:
                            tes_end_loop = 1
                "Press":
                    play sound "not_so_fast.mp3"
                    call press_witness(tes_name, tes_index) from _call_press_witness
                "Present":
                    $ evidence_index = 0
                    $ evidence_size = 4
                    if tes_name == "TSURUYA":
                        $ evidence_size = 5
                    
                    label select_evidence:
                        if evidence_index == 0:
                            $ evidence_caption = "Guy Fawkes mask and cloak\nAtypical attire. Found at the crime scene."
                        elif evidence_index == 1:
                            $ evidence_caption = "Hot dog costume\nAtypical attire. Found at the crime scene."
                        elif evidence_index == 2:
                            $ evidence_caption = "Rabbit costume\nAtypical attire. Found at the crime scene."
                        elif evidence_index == 3:
                            $ evidence_caption = "Loose photographs\nPictures of [m_1] [m_2] wearing atypical attire. Found at the crime scene.".replace("[m_1]",m_1).replace("[m_2]",m_2)
                        elif evidence_index == 4:
                            $ evidence_caption = "Infirmary records\nPaperwork indicating the comings and goings of the sick and injured. Nothing serious reported lately."
                    menu:
                        "[evidence_caption]"
                        "<":
                            $ evidence_index = (evidence_index - 1) % evidence_size
                            jump select_evidence
                        ">":
                            $ evidence_index = evidence_index = (evidence_index + 1) % evidence_size
                            jump select_evidence
                        "Present":
                            play sound "answer_me.mp3"
                            call present_evidence(tes_name, tes_index, evidence_index) from _call_present_evidence
            $ tes_line = tes_values[tes_index]

        jump tes_start
        label tes_end:
            $ tes_index = 0
            
    return
    
    label press_witness(tes_name="NONE", tes_index=0):
        if tes_name == "MIKURU":
            if tes_index == 0:
                har deskslam "What were you doing in the club room at lunch?"
                mik blink "I was going to leave some dry-cleaning."
                har -deskslam "Dry cleaning? Do tell."
                udge "Agreed. Witness, please append this to your testimony."
                $ tes_bool[1] = 1
                $ tes_bool[2] = 1
            elif tes_index == 2:
                har "I've seen your wardrobe, [m_1]."
                mik sad "So?"
                har point "You don't have anything bulky, oddly-shaped or awkward to carry."
                har think "(There's one thing she could be talking about.)"
                label bulk_accuse:
                menu:
                    "The Guy Fawkes mask and cloak":
                        har think "(Looks like it could be it, but that cloak is surprisingly lightweight.)"
                        har think "(I'll try something else.)"
                        jump bulk_accuse
                    "The hot dog costume":
                        har point "[m_1], you were carrying a hot dog suit."
                    "The rabbit costume":
                        har think "(Nope. That's about as lightweight as a rabbit costume can get.)"
                        jump bulk_accuse
                    "The loose photographs":
                        har think "(Those photos didn't exist when [m_1] was doing her dry cleaning.)"
                        jump bulk_accuse
                mik think "Ah!"
                har deskslam "So, [m_1], what were you doing with the hot dog suit?"
                har "You remember the morning, don't you?"
                mik think "Well.."
                mik "Um..."
                mik blink "..hot dog.."
                mik -blink "..hot ... dog.."
                mik sad "Ah!"
                koi deskslam "You remember something?"
                mik -sad "I remember why it was difficult to carry."
                koi bow "Grand. Do tell."
                udge "Yes, please add this to your testimony."
                $ tes_bool[2] = 0
                $ tes_bool[3] = 1
                $ tes_bool[4] = 1
            elif tes_index == 3:
                har deskslam "Why bring it in at lunch?"
                mik "I didn't have time in the morning, and didn't want to leave my delicates in the class unsupervised."
                har think "I see."
            elif tes_index == 4:
                har paper "'We' barely managed, Ms [m_2]?"
                mik "That's right, it wasn't easy."
                har deskslam "'We', Ms [m_2]?"
                mik sad "Ah!"
                har "Who else helped?"
                mik "Well.."
                mik think "Hmm.."
                koi smug "Can't remember, Ms [m_2]?"
                mik -sad "Well.. maybe.."
                mik "No, I don't remember, but we tried on outfits for a bit after."
                koi "That can't be helped. Still, the bit about trying on outfits after belongs in your testimony."
                udge "Agreed. Witness."
                $ tes_bool[5] = 1
            elif tes_index == 5:
                har "By outfits, you mean the rabbit costume, the Guy Fawkes getup, the hot dog suit, etc?"
                mik "Yep. She said that I would look like white satin and tinkling water and fairy bells all mixed up together."
                har offguard "That you would look like 'white satin and tinkling water and fairy bells all mixed up together'?"
                mik "Yep."
                har confident "[m_1], only one person talks like that."
                mik burst ".."
                har "[t_1] [t_2] helped you carry your laundry to the clubroom, and tried on outfits with you afterward."
                har think "Was she there when you passed out?"
                mik "She would have to have been, but I don't remember."
                har -confident "We'll have to speak to [t_1]."
                koi bow "The prosecution would like to propose a recess while we find Ms [t_2] to summon as a witness."
                udge "Agreed. We will reconvene in half an hour."
                $ tes_return = 1
            else:
                har offguard "Well, witness. Could you tell us more about that?"
                mik "What more is there to say?"
                udge angry "Agreed."
        elif tes_name == "TSURUYA":
            if tes_index == 0:
                har "You were carrying clothes with [m_1]?"
                tsu "That's right."
            elif tes_index == 1:
                har deskslam "'With each other'? You were wearing costumes as well?"
                tsu "That's right."
                har think "What kind of costumes?"
                tsu guarded "Some kind of rabbit suit, I think."
            elif tes_index == 2:
                har "A strange presence? You saw someone?"
                tsu "No Ma'am."
                har "You heard something?"
                tsu "No Ma'am."
                har "You felt something?"
                tsu "Yessum."
                har "What did you feel, [t_1]?"
                tsu "You know how it is when a dog is thinking about you?"
                har think ".."
                tsu "Like when you put too much oil in the wrong kettle?"
                har damage ".."
                tsu "Like when you cover your mirrors wrong?"
                har "You felt something. Let's leave it there."
            elif tes_index == 3:
                har "You were attacked? By who?"
                tsu guarded "I didn't get a good look. The assassant was in and out."
                har "Was this the same person that attacked [m_1]? Can you tell us more?"
                har think "([m_1] didn't mention a suspicious person.)"
                udge "Ms [t_2], please add details of the attacker to your testimony."
                $ tes_bool[4] = 1
                $ tes_bool[5] = 1
                $ tes_bool[8] = 1
                $ tes_bool[3] = 0
            elif tes_index == 4:
                har "Taking photos?"
                tsu offguard "Certitudinally."
                har think "(They were certainly framed like the kind of photos a deranged pervert would trespass to take.)"
            elif tes_index == 6:
                har confident "That is definitely a description of a suspicious man."
                tsu "It certainly is."
                har "They are some very conspicuous features."
                tsu "They certainly are."
                har -confident "If what you say is true, the police will have no trouble finding this man."
                tsu guarded "That's right."
                har damage ".."
            elif tes_index == 7:
                har "Witness, would you provide a few more details on this?"
                tsu "I most certainly will not."
            elif tes_index == 8:
                har "You were attacked? By the suspicious man?"
                tsu "Yupp. Meaty fists are the souls of good violence. Passed out at the door."
                har think "(She passed out in front of the door?)"
                har -think "What did he do afterwards?"
                tsu offguard "Dunno. Passed out and everything. I think he went in the club room."
                tsu "Woke up in the nurse's office after."
                har think "(I don't buy it. There's something she isn't telling us.)"
                har paper "That probably belongs in your testimony."
                udge "Agreed, witness.."
                $ tes_bool[9] = 1
            else:
                har "Witness, could you give us a few more details on that?"
                tsu guarded "Oh, but I can't think straight but everybody has been so good and kind. Aren't you very sorry for me, [h_1]? I just couldn't bear..."
                har damage "That's quite enough."
                tsu "...and you should be sorry for me. If I could blame anybody particular I would feel so much better. But what would you have done? You have such strength of mind and it's not a bit nice to faint, after all..."
                har "Judge, can you put a stop to this?"
                udge angry "[h_1], I won't make the whine culled for you."
                har "(That didn't help much.)"
    return
                
    label present_evidence(tes_name="NONE", tes_index=0, evidence_index=0):
        if tes_name == "MIKURU":
            har confident "[m_1] is lying, and this evidence proves it."
            udge "How?"
            har damage "It doesn't.."
            har think "Does this have to go on the trial logs?"
            udge "Those sheets are a trusted record of exactly what has happened today."
            udge angry "[h_1], I won't change the sheets for you."
        elif tes_name == "TSURUYA":
            if tes_index == 4 and evidence_index == 3:#photo
                har confident "Ms [t_2], this isn't a real court, but we still expect the truth from you."
                har paper "What you're telling us doesn't line up with these photos."
                udge "I see no contradiction."
                har "There's nothing wrong with what's in the photos."
                har "The problem lies with what isn't. Ms [t_2] isn't in a single one of these."
                tsu offguard "Ah!"
                har "[t_1] and [m_1] were trying on costumes together."
                har point "[t_1], do you really expect us to believe that your mysterious pervert was keeping you out of frame?"
                tsu "Ah!"
                tsu offguard "You mean I didn't explain."
                tsu guarded "I'll have to add it to my testimony."
                udge "Witness, please add it to your testimony. It is important that you include ALL relevant details."
                tsu guarded"Yahup."
                $ tes_bool[6] = 1
                $ tes_bool[7] = 1
            elif tes_index == 9 and evidence_index == 4:#infirmary records
                har confident "That's mighty odd, Ms [t_2]."
                tsu "..?"
                har "I happen to have the infirmary records here, and they make no reference to an unconcious girl."
                tsu offguard "Ah!"
                koi smug "Not so fast. Plenty of students use the facilities without filling the proper paperwork."
                har deskslam "You can't be unconscious the whole afternoon without someone from the staff noticing."
                koi deskslam "Nobody said she was there after lunch."
                koi point "[t_1] attended her classes all afternoon."
                tsu guarded "Indeed I did. Not so freckled as it looks now, huh?"
                har think "Hmm.."
                har -think "You mean you didn't go back to check on [m_1]?"
                har point "You would think one would have to be really bad and unregenerate to leave her after that."
                har confident "I think we can dismiss Ms [t_2]'s testimony."
                $ tes_return = 1
            else:
                har confident "[t_1] is lying, and this evidence proves it."
                udge "It really doesn't."
                tsu guarded "Don’t speak of this to me again! Whatever put such an idea into your head? How dare you say such things about me?"
                har damage "([t_1] surely has a very bad temper. [t_1] surely must learn to control her temper.)"
