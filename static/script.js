var quotes = [
  "O son of Kunti, the nonpermanent appearance of happiness and distress, and their disappearance in due course, are like the appearance and disappearance of winter and summerseasons. They arise from sense perception, O scion of Bharata, and one must learn to tolerate them without being disturbed. ~Source: Bhagavad-Geeta 2.14",
  "For the soul there is neither birth nor death at any time. He has not come into being, does not come into being, and will not come into being. He is unborn, eternal,ever-existing, and primeval. He is not slain when the body is slain. ~Source: Bhagavad-Geeta 2.20",
  "One who is not disturbed in mind even amidst the threefold misery or elated when there is happiness, and who is free from attachment, fear and anger, is called a sage of steadymind. ~Source: Bhagavad-Geeta 2.56",
  "What is night for all beings is the time of awakening for the self-controlled; and the time of awakening for all beings is night for the introspective sage. ~Source: Bhagavad-Geeta 2.69",
  "The thoughts of My pue devotee dwell in Me, their lives are fully devoted to My service, and they derive great satisfaction and bliss from always enlightening one another andconversing about Me. ~Source: Bhagavad-Geeta 10. 9",
  "One who knows the transcendental nature of My appearance and activities does not, upon leaving the body, take birth again in this material world, but attains My eternal abode,O Arjuna. ~Source: Bhagavad-Geeta 4.9",
  "As a lamp in a windless place does not waver, so the transcendentalist, whose mind is controlled, remains always steady in his meditation on the transcendent self. ~Source: Bhagavad-Geeta 6.19",
  "For one who sees me everywhere and sees everything in Me, I am never lost, nor is he ever lost to me. ~Source: Bhagavad-Geeta 6.30",
  "There is no truth superior to Me. Everything rests upon Me, as pearls are strung on a thread. ~Source: Bhagavad Geeta 7.7",
  "After many births and deaths, he who is actually in knowledge surrenders unto Me, knowing Me to be the cause of all causes and all that is. Such a great soul is very rare. ~Source: Bhagavad-Geeta 7.19",
  "Those who fix their minds on My personal form and are always engaged in worshiping Me with great and transcendental faith are considered by Me to be most perfect. ~Source: Bhagavad-Geeta 12.2",
  "Whoever knows Me as the Supreme Personality of Godhead, without doubting, is the knower of everything. He therefore engages himself in full devotional service to Me, O son ofBharata. ~Source: Bhagavad-Geeta 15.19",
  "I envy no one, nor I partial to anyone. I am equal to all. But whoever renders service unto Me in devotion is a friend, is in Me, and I am also friend to him. ~Source: Bhagvad-Geeta 9. 29",
  "I am the source of all spiritual and material world. Everything emanates from Me. The wise who perfectly know this engage in My devotional service and worship Me with all theirhearts. ~Source: Bhagvad-Geeta 10. 8",
  "My dear Arjuna, he who engages in My pure devotional service, free from the contaminations of fruitive activities and mental speculation, he who works for Me, who makes Me thesupreme goal of life, and who is friendly to every living being- he certainly comes to Me. ~Source: Bhagvad-Geeta 11. 55",
  "If you cannot practice the regulations of bhakti-yoga, then just try to work for Me, because by working for Me you will come to the perfect stage. ~Source: Bhagvad-Geeta 12.10",
  "One who engages in full devotional service, unfailing in all circumstances, at once transcends the modes of material nature and thus comes to the level of Brahman. ~Source: Bhagvad-Geeta 14.26",
  "The living entities in this conditioned world are My eternal fragmentary parts. Due to the conditioned life , they are struggling very hard with the six senses which includethe mind. ~Source: Bhagvad-Geeta 15.7",
  "If you become conscious of Me, you will passover all the obstacles of conditioned life by My grace. If however you do not work in such consciousness but act through false ego,not hearing Me, you will be lost. ~Source: Bhagvad-Geeta 18.58",
  "Abandon all varieties of religion and just surrender unto Me. I shall deliver you from all sinful reactions. Do not fear. ~Source: Bhagvad-Geeta 18.66"
  ];
  
const randomQuote = quotes[Math.floor(Math.random() * quotes.length)];
console.log(randomQuote);

  
const dia = document.querySelector(".dia");
  const quoteElement = document.getElementById("quote");
  quoteElement.textContent = randomQuote;

const loading = document.getElementById('loading');
const form = document.querySelector('form');

form.addEventListener('submit', () => {
  loading.style.display = 'block';
});



const textarea = document.querySelector('textarea');

textarea.addEventListener('input', () => {
  textarea.style.height = 'auto';
  textarea.style.height = textarea.scrollHeight + 'px';
});



function scrollToEnd() {
  window.scrollTo({
    top: document.body.scrollHeight,
    behavior: 'smooth'
  });
};

const submitButton = document.getElementById('submit');
submitButton.addEventListener('click', () => {
  const bodyHeight = document.body.scrollHeight;
  window.scrollTo(0, bodyHeight);
});



// document.getElementById("submit").addEventListener("click", scrollToEnd());


var animationContainer = document.getElementById('loading');
var animationDataUrl = 'https://assets1.lottiefiles.com/packages/lf20_chhegoln.json';

var animData = {
  container: animationContainer,
  renderer: 'svg',
  loop: true,
  autoplay: true,
  path: animationDataUrl
};

var anim = bodymovin.loadAnimation(animData);




