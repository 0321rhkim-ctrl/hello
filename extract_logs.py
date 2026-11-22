import re
from pathlib import Path


def main():
    log_path = Path("log.txt")
    if not log_path.exists():
        raise FileNotFoundError(
            "현재 폴더에 log.txt 파일이 없습니다. 로그 내용을 log.txt로 저장해 주세요."
        )

    text = log_path.read_text(encoding="utf-8")

    emails = re.findall(
        r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)+\b",
        text,
    )

    phones = re.findall(
        r"(?<!\d)010[-.\s]\d{4}[-.\s]\d{4}(?!\d)",
        text,
    )

    students = re.findall(
        r"\[\s*(202\d{6})\s*/\s*([^\[\]/]+?)\s*\]",
        text,
    )

    github_repos = re.findall(
        r"https?://(?:www\.)?github\.com/[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+",
        text,
    )
    coupons_2026 = re.findall(
        r"\bFEST-2026-[A-Za-z0-9]{4}\b",
        text,
    )

    sales_raw = re.findall(r"매출\s*:\s*([0-9,]+)\s*원?", text)
    sales_list = [int(amount.replace(",", "")) for amount in sales_raw]
    total_sales = sum(sales_list)

    print("1. 유효한 이메일:", emails)
    print("2. 휴대폰 번호:", phones)
    print("3. 재학생 (학번, 학과):", students)
    print("4-1. GitHub 저장소:", github_repos)
    print("4-2. 2026 유효 쿠폰:", coupons_2026)
    print("5. 부스별 매출:", sales_list, "/ 총 매출 합계:", f"{total_sales:,}원")


if __name__ == "__main__":
    main()
