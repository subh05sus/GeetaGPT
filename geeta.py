import random


quotes=[
"O son of Kunti, the nonpermanent appearance of happiness and distress, and their disappearance in due course, are like the appearance and disappearance of winter and summerseasons. They arise from sense perception, O scion of Bharata, and one must learn to tolerate them without being disturbed.  ~ Source: Lord Sri Krsna - Bhagavad-gita 2.14",
"For the soul there is neither birth nor death at any time. He has not come into being, does not come into being, and will not come into being. He is unborn, eternal,ever-existing, and primeval. He is not slain when the body is slain.  ~ Source: Lord Sri Krsna - Bhagavad-gita 2.20",
"One who is not disturbed in mind even amidst the threefold misery or elated when there is happiness, and who is free from attachment, fear and anger, is called a sage of steadymind.  ~ Source: Lord Sri Krsna - Bhagavad-gita 2.56",
"What is night for all beings is the time of awakening for the self-controlled; and the time of awakening for all beings is night for the introspective sage.  ~ Source: Lord Sri Krsna - Bhagavad-gita 2.69",
"The thoughts of My pue devotee dwell in Me, their lives are fully devoted to My service, and they derive great satisfaction and bliss from always enlightening one another andconversing about Me.  ~ Source: Lord Sri krsna - Bhagavad-gita 10. 9",
"One who knows the transcendental nature of My appearance and activities does not, upon leaving the body, take birth again in this material world, but attains My eternal abode,O Arjuna.  ~ Source: Lord Sri Krsna - Bhagavad-gita 4.9",
"As a lamp in a windless place does not waver, so the transcendentalist, whose mind is controlled, remains always steady in his meditation on the transcendent self.  ~ Source: Lord Sri Krsna - Bhagavad-gita 6.19",
"For one who sees me everywhere and sees everything in Me, I am never lost, nor is he ever lost to me.  ~ Source: Lord Sri Krsna - Bhagavad-gita 6.30",
"There is no truth superior to Me. Everything rests upon Me, as pearls are strung on a thread.  ~ Source: Lord Sri Krsna - Bhagavad gita 7.7",
"After many births and deaths, he who is actually in knowledge surrenders unto Me, knowing Me to be the cause of all causes and all that is. Such a great soul is very rare.  ~ Source: Lord Sri Krsna - Bhagavad-gita 7.19",
"Those who fix their minds on My personal form and are always engaged in worshiping Me with great and transcendental faith are considered by Me to be most perfect.  ~ Source: Lord Sri Krsna - Bhagavad-gita 12.2",
"Whoever knows Me as the Supreme Personality of Godhead, without doubting, is the knower of everything. He therefore engages himself in full devotional service to Me, O son ofBharata.  ~ Source: Lord Sri Krsna - Bhagavad-gita 15.19",
"I envy no one, nor I partial to anyone. I am equal to all. But whoever renders service unto Me in devotion is a friend, is in Me, and I am also friend to him.  ~ Source: Lord Sri Krishna - Bhagvad-gita 9. 29",
"I am the source of all spiritual and material world. Everything emanates from Me. The wise who perfectly know this engage in My devotional service and worship Me with all theirhearts.  ~ Source: Lord Sri Krishna - Bhagvad-gita 10. 8",
"My dear Arjuna, he who engages in My pure devotional service, free from the contaminations of fruitive activities and mental speculation, he who works for Me, who makes Me thesupreme goal of life, and who is friendly to every living being- he certainly comes to Me.  ~ Source: Lord Sri Krishna - Bhagvad-gita 11. 55",
"If you cannot practice the regulations of bhakti-yoga, then just try to work for Me, because by working for Me you will come to the perfect stage.  ~ Source: Lord Sri Krishna - Bhagvad-gita 12.10",
"One who engages in full devotional service, unfailing in all circumstances, at once transcends the modes of material nature and thus comes to the level of Brahman.  ~ Source: Lord sri Krishna - Bhagvad-gita 14.26",
"The living entities in this conditioned world are My eternal fragmentary parts. Due to the conditioned life , they are struggling very hard with the six senses which includethe mind.  ~ Source: Lord Sri Krishna - Bhagvad-gita 15.7",
"If you become conscious of Me, you will passover all the obstacles of conditioned life by My grace. If however you do not work in such consciousness but act through false ego,not hearing Me, you will be lost.  ~ Source: Lord Sri Krishna - Bhagvad-gita 18.58",
"Abandon all varieties of religion and just surrender unto Me. I shall deliver you from all sinful reactions. Do not fear.  ~ Source: Lord Sri Krishna - Bhagvad-gita 18.66"
"Blessed is a human birth, even the dwellers in heaven desire this birth, for true knowledge and pure love may be attained only by a human being." 
"The Key to happiness is the reduction of desires."
"No one who does good work will ever come to a bad end, either here or in the world to come."
"The peace of God is with them whose mind and soul are in harmony, who are free from desire and wrath, who know their own soul." 
"We behold what we are, and we are what we behold."
"Even as a person casts off worn-out clothes and puts on others that are new, so the embodied self casts off worn-out bodies and enters into others that are new."
"As fire is concealed by smoke, as a mirror by dust, as an unborn baby by the womb, so is knowledge concealed by ignorance."
"The self-controlled soul, who moves amongst sense objects, free from either attachment or repulsion, he wins eternal Peace."
"Never was there a time when I did not exist, nor you, nor these kings of men. Never will there be a time hereafter when any of us shall cease to be." 
"Even as the embodied self passes, in this body, through the stages of childhood, youth, and old age, so does it pass into another body. Calm souls are not bewildered by this." 
"Notions of heat and cold, of pain and pleasure. arise, O son of Kunti, only from the contact of the senses with their objects. They come and go; they are impermanent, endure them, O Bharata." 
"Being established in Yoga, O Dhananjaya, perform your actions, casting off attachment and remaining even-minded both in success and in failure. This evenness is called Yoga." 
"The man of self-control, moving among objects with his senses under restraint, and free from attachment and hate, attain serenity of mind." 
"That man who lives completely free from desires, without longing, devoid of the sense of 'I' and 'mine,' attains peace." 
"Therefore always do without attachment the work you have to do; for a man who does his work without attachment attains the Supreme." 
"The love and hatred that the senses feel for their objects are inevitable. But let no one come under their sway; for they are one’s enemies." 
"He who has no attachments can really love others, for his love is pure and divine." - Bhagavad Gita 5.29
"Strive constantly to serve the welfare of the world; by devotion to selfless work, one attains the supreme goal of life." - Bhagavad Gita 3.19
"The wise see knowledge and action as one; they see truly." - Bhagavad Gita 5.4
"The soul is neither born, and nor does it die. It is not slain when the body is slain." - Bhagavad Gita 2.20
"Those who are free from anger and all material desires, who are self-realized, self-disciplined and constantly endeavoring for perfection, are assured of liberation in the Supreme." - Bhagavad Gita 5.26
"Set thy heart upon thy work, but never on its reward." - Bhagavad Gita 2.47
"A person can rise through the efforts of his own mind; or draw himself down, in the same manner. Because each person is his own friend or enemy in either the face of adversity or opportunity." - Bhagavad Gita 6.5-6
"He who is not disturbed in mind even amidst the threefold miseries or elated when there is happiness, and who is free from attachment, fear, and anger, is called a sage of steady mind." - Bhagavad Gita 2.56
"The one who has control over his mind is tranquil in heat and cold, in pleasure and pain, and in honor and dishonor; and is ever steadfast with the Supreme Self." - Bhagavad Gita 6.7
"Perform your duties with an unperturbed mind, O Arjuna, abandoning all desires for any benefit and being content with whatever comes your way, for such a person is unaffected by sinful reactions, even as a lotus leaf is untouched by water." - Bhagavad Gita 2.47
"Detached action is selfless action. You can be detached while doing your duties, and that is the secret of selfless action." - Bhagavad Gita 3.19
"The senses are so strong and impetuous, O Arjuna, that they forcibly carry away the mind even of a man of discrimination who is endeavoring to control them." - Bhagavad Gita 2.60
"In the material world, the wise are engaged in charity and acts of welfare for the welfare of others. In this way, they achieve liberation from the cycle of birth and death." - Bhagavad Gita 5.25
"I am time, the great destroyer of the world, and I have come here to destroy all people. With the exception of you [the Pandavas], all the soldiers here on both sides will be slain." - Bhagavad Gita 11.32
"One who is not disturbed by the incessant flow of desires—that enter like rivers into the ocean, which is ever being filled but is always still—can alone achieve peace, and not the person who strives to satisfy such desires." - Bhagavad Gita 2.70
"Abandoning all desires born of egoism, and completely restraining the mind with the intellect, they live free from the sense of 'I' and 'mine,' and attain the state of peace beyond all understanding." - Bhagavad Gita 2.71
"I am the beginning, the middle, and the end of all beings." - Bhagavad Gita 10.20
"Perform your prescribed duties, for action is better than inaction. A man cannot even maintain his physical body without work." - Bhagavad Gita 3.8
"For those who are constantly devoted and who worship Me with love, I give the understanding by which they can come to Me." - Bhagavad Gita 10.10
"Those who are not deluded, the great souls, are under the protection of the divine nature. They are fully engaged in devotional service because they know Me as the Supreme Personality of Godhead, original and inexhaustible." - Bhagavad Gita 9.13
"Abandon all varieties of religion and just surrender unto Me. I shall deliver you from all sinful reactions. Do not fear.  ~ Source: Lord Sri Krishna - Bhagvad-gita 18.66",
"Blessed is a human birth, even the dwellers in heaven desire this birth, for true knowledge and pure love may be attained only by a human being.",
"The key to happiness is the reduction of desires.",
"The peace of God is with them whose mind and soul are in harmony, who are free from desire and wrath, who know their own soul.",
"Perform your duties with an unperturbed mind, O Arjuna, abandoning all desires for any benefit and being content with whatever comes your way, for such a person is unaffected by sinful reactions, even as a lotus leaf is untouched by water."
];

random_quote = random.choice(quotes)

