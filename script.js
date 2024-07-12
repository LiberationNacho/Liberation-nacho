document.addEventListener('DOMContentLoaded', function() {
    // 페이지가 로드되면 실행될 함수를 등록한다. DOMContentLoaded 이벤트는 HTML 문서의 모든 요소가 로드되었을 때 발생한다.
  
    // JSON 파일을 fetch() 함수로 가져오기
    fetch('attainment.json')
        .then(response => response.json()) // JSON 형식의 응답을 자바스크립트 객체로 변환한다.
        .then(data => {
            const characters = Object.values(data); // JSON 데이터에서 캐릭터 배열을 추출한다.
  
            // HTML 테이블에 데이터 삽입
            const tableBody = document.getElementById('characterData'); // 캐릭터 데이터를 넣을 테이블의 tbody 요소를 가져온다.
            characters.forEach(character => {
                const row = document.createElement('tr'); // 각 캐릭터에 대한 새로운 행(tr) 요소를 생성한다.
                row.innerHTML = `
                    <td>${character.Name}</td>
                    <td>${parseInt(character.Combat).toLocaleString()}</td>
                    <td><img src="${character.image}" alt="${character.Name}"></td>
                    <td>${character.liberation}</td>
                    <td>${character['1b']}</td>
                `; // 각 캐릭터의 정보를 테이블 셀(td)에 넣는다.
                tableBody.appendChild(row); // 생성한 행을 테이블에 추가한다.
            });
        })
        .catch(error => {
            console.error('Error fetching JSON:', error); // JSON 가져오기 오류가 발생한 경우 콘솔에 오류 메시지를 출력한다.
        });
  
    fetch('result.json')
        .then(response => response.json())
        .then(data => {
            // JSON 파일에서 새로운 기준일과 달성률을 가져옵니다.
            const newDate = data.Date;
            const jobAchievementRate = data.JobRate * 100;
            const liberationAchievementRate = data.Liberation_Rate * 100;
            const sumLevel = data.Sum_Level;
            const sumCombat = data.Sum_Combat;
            const avgLevel = data.Avg_Level;
            const avgCombat = data.Avg_Combat;
  
            // 기준일을 표시하는 <p> 요소를 찾습니다.
            const dateParagraph = document.querySelector('.info p');
  
            // <p> 요소의 텍스트를 새로운 기준일로 업데이트합니다.
            dateParagraph.textContent = `기준일 : ${newDate}`;
  
            // 전직업 및 해방 달성률을 표시할 <div> 요소를 찾습니다.
            const statsDiv = document.querySelector('.stats');
            statsDiv.innerHTML += `
                <p>전직업 1억 달성률: <strong>${jobAchievementRate.toFixed(2)}%</strong>, 전직업 해방 달성률: <strong>${liberationAchievementRate.toFixed(2)}%</strong></p>
                <p>총 레벨 합계: <strong>${sumLevel.toLocaleString()}</strong>, 총 전투력 합계: <strong>${sumCombat.toLocaleString()}</strong></p>
                <p>평균 레벨: <strong>${avgLevel.toFixed(2)}</strong>, 평균 전투력: <strong>${avgCombat.toFixed(2)}</strong></p>
            `; // 계산된 달성률과 추가된 데이터를 HTML에 추가한다.
        })
        .catch(error => console.error('JSON 데이터를 가져오는 중 오류 발생:', error));
});
