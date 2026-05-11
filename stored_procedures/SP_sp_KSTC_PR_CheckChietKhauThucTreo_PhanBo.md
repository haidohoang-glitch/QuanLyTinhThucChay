# Stored Procedure: `sp_KSTC_PR_CheckChietKhauThucTreo_PhanBo`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2021-06-05 10:06:11.917000
- **Ngày sửa cuối**: 2025-09-03 10:17:02.577000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[sp_KSTC_PR_CheckChietKhauThucTreo_PhanBo]
	-- Add the parameters for the stored procedure here
	
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	SELECT 'NGUON' [NoiCheck],
       B.*,
       A.*
	   ,(CONVERT(FLOAT,A.ChietKhauThucTreo) -B.ChietKhauhd) [Lech_CkTreo - CkHd]
FROM
(
    SELECT id,
           CONVERT(FLOAT,ChietKhau) AS ChietKhauThucTreo,
           Contract_Detail_Id
    FROM [ASDAG2].ThucTreo.dbo.ThucTreo_PR
    WHERE Deleted_Status = 0
) A
    INNER JOIN
    (
        SELECT hd.CONTRACT_NUMBER,
               hdct.ID HopDongChiTietID,
               hdct.PERCENT_DISCOUNT_TOTAL AS ChietKhauhd,
               hdct.LAST_MODIFIED_AT
        FROM [ASDAG2].CONTRACT.dbo.CONTRACTS hd
            INNER JOIN [ASDAG2].CONTRACT.dbo.CONTRACT_DETAILS hdct
                ON hd.ID = hdct.CONTRACT_ID
        WHERE 1 = 1
              AND hdct.DELETED_STATUS = 0
              AND hd.CONTRACT_YEAR >= 2020
    ) B
        ON A.Contract_Detail_Id = B.HopDongChiTietID
WHERE ABS(CONVERT(FLOAT,A.ChietKhauThucTreo) -B.ChietKhauhd)>0.1;

SELECT 'DICH' [NoiCheck],
       B.*,
       A.*
FROM
(
    SELECT ChietKhau AS ChietKhauThucTreo,
           HopDongChiTietREF
    FROM ThucChayHopDongChiTietPR
    WHERE DeletedStatus = 0
) A
    INNER JOIN
    (
        SELECT hd.SoHopDong,
               hd.HopDongID,
               hdct.HopDongChiTietID,
               hdct.ChietKhau AS ChietKhauhd,
               hdct.LastModifiedAt
        FROM HopDong hd
            INNER JOIN HopDongChiTiet hdct
                ON hd.HopDongID = hdct.HopDongFK
        WHERE 1 = 1
              AND hdct.DeletedStatus = 0
              AND hd.Nam >= 2020
    ) B
        ON A.HopDongChiTietREF = B.HopDongChiTietID
WHERE NOT ROUND(A.ChietKhauThucTreo, 4) = ROUND(B.ChietKhauhd, 4);
END

```
