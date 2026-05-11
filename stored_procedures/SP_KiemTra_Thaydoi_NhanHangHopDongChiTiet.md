# Stored Procedure: `KiemTra_Thaydoi_NhanHangHopDongChiTiet`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2018-05-15 09:27:42.690000
- **Ngày sửa cuối**: 2024-10-05 11:35:26.530000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@Day_Check` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================================================
-- Author:		hungtruongviet
-- Create date: 14/5/2018
-- Description:	Check nhãn hàng đánh số từ 2017 của phần bổ DB : ABM và CONTRACT
-- ==============================================================================
/*
EXEC [dbo].[KiemTra_Thaydoi_NhanHangHopDongChiTiet] 1
*/


CREATE PROCEDURE [dbo].[KiemTra_Thaydoi_NhanHangHopDongChiTiet]
					@Day_Check int = '700'
AS
BEGIN
	SELECT [HopDongChiTietID],
		   [DanhSachNhanHangREF_ABM]
	INTO #T1
	FROM
	(
		SELECT A.[HopDongChiTietID] [HopDongChiTietID],
			   A.[DanhSachNhanHangREF] [DanhSachNhanHangREF_ABM]
		FROM
		(
			SELECT [HopDongChiTietID],
				   [HopDongFK],
				   [DanhSachNhanHangREF]
			FROM dbo.[HopDongChiTiet]
			WHERE [DeletedStatus] = 0
		) A
		INNER JOIN
		(
			SELECT	[HopDongID],
					[NgayDanhSoHopDong]
			FROM dbo.[HopDong]
			WHERE [DeletedStatus] = 0
					AND [NgayDanhSoHopDong] > ( DATEADD (day, -@Day_Check, GETDATE()) )
		) B
			ON A.[HopDongFK] = B.[HopDongID]
	) T;

	SELECT [ContractDetailID],
		   [DanhSachNhanHang_CONTRACT]
	INTO #T2
	FROM
	(
		SELECT DISTINCT
			   B.ID [ContractDetailID],
			   STUFF(
			   (
				   SELECT  ',' + CONVERT(VARCHAR(50), C0.[DmNhanHangID])
				   FROM
				   (
					   SELECT [BRAND_ID],
							  [CONTRACT_DETAIL_ID],
							  [DELETED_STATUS]
					   FROM [ASDAG2].[CONTRACT].dbo.[CONTRACT_DETAIL_BRANDS]
				   ) C1
					   JOIN
					   (
						   SELECT [DmNhanHangID],
								  [DeletedStatus]
						   FROM [ASDAG2].[CONTRACT].dbo.[DmNhanHang]
					   ) C0
						   ON C1.[BRAND_ID] = C0.[DmNhanHangID]
							  AND C1.[DELETED_STATUS] = 0
							  AND C0.[DeletedStatus] = 0
				   WHERE C1.[CONTRACT_DETAIL_ID] = B.[ID]
				   FOR XML PATH('')
			   ),
			   1,
			   1,
			   ''
					) [DanhSachNhanHang_CONTRACT]
		FROM
		(
			SELECT [ID],
				   [CONTRACT_ID],
				   [DELETED_STATUS]
			FROM [[ASDAG2]].[CONTRACT].[dbo].[CONTRACT_DETAILS]
		) B
			INNER JOIN
			(
				SELECT [ID],
					   [DELETED_STATUS],
					   [INDEXED_DATE]
				FROM [[ASDAG2]].[CONTRACT].[dbo].[CONTRACTS]
			) C
				ON B.[CONTRACT_ID] = C.ID
				   AND C.[DELETED_STATUS] = 0
				   AND B.[DELETED_STATUS] = 0
		WHERE C.[INDEXED_DATE] >  (DATEADD (day, -@Day_Check, GETDATE())) 
	) T;

	TRUNCATE TABLE KiemTraNhanHangThayDoi
	Insert Into KiemTraNhanHangThayDoi
	SELECT #T1.[HopDongChiTietID]			,
		   #T1.[DanhSachNhanHangREF_ABM]	,
		   #T2.[DanhSachNhanHang_CONTRACT]	,
			'' [Warring]
		FROM #T1
		INNER JOIN #T2
		ON #T1.HopDongChiTietID = #T2.ContractDetailID
	WHERE #T1.[DanhSachNhanHangREF_ABM] <> #T2.[DanhSachNhanHang_CONTRACT]
	DROP TABLE #T1, #T2
END

```
