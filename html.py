<div id="ff-profile" style="background: #111; color: #fff; padding: 20px; border-radius: 10px; width: 300px; border: 1px solid #ff4757;">
    <h3 style="color: #ff4757; margin-top: 0;">Player Info</h3>
    <p><strong>Account ID:</strong> <span id="accId">Loading...</span></p>
    <p><strong>Nickname:</strong> <span id="nick">Loading...</span></p>
    <p><strong>Region:</strong> <span id="reg">Loading...</span></p>
    <p><strong>Level:</strong> <span id="lvl">Loading...</span></p>
    <p><strong>BR Points:</strong> <span id="br">Loading...</span></p>
    <p><strong>Liked:</strong> <span id="likes">Loading...</span></p>
    <p><strong>CS Points:</strong> <span id="cs">Loading...</span></p>
</div>

<script>
    // এই ফাংশনটি সরাসরি আপনার API থেকে ডেটা টানবে
    async function getRealData() {
        const uid = "5513136279"; // আপনার দেওয়া UID
        try {
            const response = await fetch(`https://mahfuj.vercel.app/api/ffinfo?uid=${uid}`);
            const data = await response.json();
            
            const info = data.basicInfo;

            // খালি জায়গাগুলো রিয়েল ডেটা দিয়ে পূরণ করা হচ্ছে
            document.getElementById('accId').innerText = info.accountId;
            document.getElementById('nick').innerText = info.nickname;
            document.getElementById('reg').innerText = info.region;
            document.getElementById('lvl').innerText = info.level;
            document.getElementById('br').innerText = info.rankingPoints;
            document.getElementById('likes').innerText = info.liked;
            document.getElementById('cs').innerText = info.csRankingPoints;
            
        } catch (error) {
            console.error("ডেটা আনতে সমস্যা হয়েছে:", error);
        }
    }

    getRealData();
</script>