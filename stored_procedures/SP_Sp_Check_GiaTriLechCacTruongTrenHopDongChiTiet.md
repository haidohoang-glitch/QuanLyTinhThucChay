# Stored Procedure: `Sp_Check_GiaTriLechCacTruongTrenHopDongChiTiet`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-02-22 14:46:14.803000
- **Ngày sửa cuối**: 2017-03-11 09:42:11.843000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayBatDau` | `nvarchar(100)` | No |
| `@NgayKetThuc` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
--Sp_Check_GiaTriLechCacTruongTrenHopDongChiTiet '2017-03-08','2017-03-10'
CREATE PROCEDURE [dbo].[Sp_Check_GiaTriLechCacTruongTrenHopDongChiTiet]
    @NgayBatDau NVARCHAR(50) ,
    @NgayKetThuc NVARCHAR(50)
AS
    BEGIN

        DECLARE @LastSynTime DATETIME
        DECLARE @MaxTimeSynInHD DATETIME
        DECLARE @FromDate DATETIME
        SET @MaxTimeSynInHD = ( SELECT  MAX(LastModifiedAt)
                                FROM    dbo.HopDongChiTiet
                              )

        IF @NgayKetThuc = ''
            SET @LastSynTime = GETDATE()
        ELSE
            SET @LastSynTime = @NgayKetThuc
        IF @NgayBatDau = ''
            SET @FromDate = DATEADD(DD, -2, @LastSynTime)
        ELSE
            SET @FromDate = @NgayBatDau
      
		
		
        CREATE TABLE #HopDongChiTietTemp
            (
			  id INT,
              hd_id INT ,
              abm_nhanhang_id NVARCHAR(2000) ,
              nhanhang NVARCHAR(1000) ,
              loai_id int ,
              TenHinhThucQC NVARCHAR(1000) ,
              Loaihinh_id INT ,
              TenSanPham NVARCHAR(200) ,
              website_id INT ,
              Tenwebsite NVARCHAR(300) ,
              loai_banner_id INT ,
              DmLoaiNenTangREF INT ,
              thoigian_val DATETIME ,
              thoigian_unit DATETIME ,
              giatri FLOAT ,
              chietkhau FLOAT ,
              thanhtien FLOAT ,
              iskhuyenmai INT ,
              Tk_AdmarketID NVARCHAR(50) ,
              TK_Admarket NVARCHAR(50) ,
              CKMua FLOAT,
			  LastModifiedAt DATETIME
            )

        DECLARE @SQL NVARCHAR(MAX) 
		
        SET @SQL = 'select A.* from hdcn_phanbosite A inner join hdcn_hd B on B.id=A.hd_id  
					where CONVERT(A.LastModifiedAt,DATE) between '''''
					+ CONVERT(NVARCHAR(20), @FromDate, 120) + ''''' AND '''''
					+ CONVERT(NVARCHAR(20), @LastSynTime, 120) + '''''
					;'
        SET @SQL = '
					SELECT	id,
							hd_id ,
							isnull(abm_nhanhang_id,0) ,
							nhanhang ,
							loai_id ,
							TenHinhThucQC ,
							Loaihinh_id ,
							TenSanPham ,
							website_id ,
							Tenwebsite ,
							loai_banner_id ,
							DmLoaiNenTangREF ,
							thoigian_val ,
							thoigian_unit ,
							giatri ,
							chietkhau ,
							thanhtien ,
							iskhuyenmai ,
							Tk_AdmarketID ,
							TK_Admarket ,
							CKMua,
							LastModifiedAt
					FROM OPENQUERY(MySQL,''' + @SQL + ''') 
					'
        PRINT @SQL
        INSERT  #HopDongChiTietTemp
                EXECUTE ( @SQL
                       )
        DECLARE @TotalRows INT
        DECLARE @x INT
        DECLARE @ColumnSQL NVARCHAR(500)
        DECLARE @ColumnMySQL NVARCHAR(500)
        DECLARE @DoiTuong NVARCHAR(500)
        SET @TotalRows = ( SELECT   MAX(STT)
                           FROM     ColumnCheckValue
                           WHERE    DoiTuong = N'Hợp đồng chi tiết'
                         )
        SET @x = 2
        WHILE @x <= @TotalRows
            BEGIN
                SELECT  @ColumnSQL = ColumnSQL
                FROM    ColumnCheckValue A
                WHERE   STT = @x
                        AND DoiTuong = N'Hợp đồng chi tiết'
                SELECT  @ColumnMySQL = ColumnMySQL
                FROM    ColumnCheckValue A
                WHERE   STT = @x
                        AND DoiTuong = N'Hợp đồng chi tiết'
                SELECT  @DoiTuong = DoiTuong
                FROM    ColumnCheckValue
                WHERE   STT = @x
                        AND DoiTuong = N'Hợp đồng chi tiết'
                SET @SQL = '
			SELECT  ''' + @ColumnSQL + ''' [Column], 
					N''' + @DoiTuong + ''' DoiTuong, 
					B.HopDongChiTietID,
					B.' + @ColumnSQL + ' DulieuSQL,
					A.' + @ColumnMySQL + ' DulieuMySQL,
					''Lech du lieu'' LoaiVanDe,
					''' + CONVERT(NVARCHAR(100), GETDATE(), 113)
                    + ''' ThoiGianLog,
					0 TrangThaiXuLy,
					14 IDLoai
			FROM    #HopDongChiTietTemp A FULL JOIN
			(
			SELECT  *
			FROM    dbo.HopDongChiTiet
			WHERE   CONVERT(DATE,LastModifiedAt) BETWEEN  '''
                    + CONVERT(NVARCHAR(100), @FromDate, 113) + ''' AND '''
                    + CONVERT(NVARCHAR(100), @LastSynTime, 113) + '''
			) B ON A.id=B.HopDongChiTietID
			WHERE 1=1 
			AND B.' + @ColumnSQL + '<> A.' + @ColumnMySQL + '
			AND A.LastModifiedAt <=''' + CONVERT(NVARCHAR(50), @MaxTimeSynInHD, 113)
                    + ''''
                INSERT  INTO CheckThongTinDauVao
                        EXECUTE ( @SQL
                               )
                SET @x = @x + 1
            END
		
    END
	--Sp_Check_GiaTriLechCacTruongTrenHopDongChiTiet '',''

```
